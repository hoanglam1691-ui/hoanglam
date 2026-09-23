#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI4A: Operations Analyst Data Processing Engine
Skill: ai4a:ops-analyst
"""

import os
import sys
import csv
import json
import re
import unicodedata
from datetime import datetime

def slugify(text: str) -> str:
    if not text:
        return "Unassigned"
    # replace Vietnamese đ/Đ
    text = text.replace('đ', 'd').replace('Đ', 'D')
    # normalize NFKD
    nfkd = unicodedata.normalize('NFKD', text)
    ascii_text = ''.join([c for c in nfkd if not unicodedata.combining(c)])
    slug = re.sub(r'[^a-zA-Z0-9]', '_', ascii_text)
    slug = re.sub(r'_+', '_', slug)
    return slug.strip('_')

def standardize_status(raw_status: str) -> str:
    if not raw_status:
        return "In Progress"
    raw_status = raw_status.strip().lower()
    if any(k in raw_status for k in ['completed', 'hoan thanh', 'xong', 'done', 'closed']):
        return "Completed"
    elif any(k in raw_status for k in ['delayed', 'tre', 'qua han', 'late', 'overdue']):
        return "Delayed"
    elif any(k in raw_status for k in ['cancelled', 'huy', 'that bai', 'failed']):
        return "Cancelled"
    return "In Progress"

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "sample-data/erp_operations_sample.csv"
    target_month = sys.argv[2] if len(sys.argv) > 2 else ""

    if not os.path.exists(input_path):
        print(f"Error: File not found at {input_path}")
        sys.exit(1)

    dept_dir = "outputs/departments"
    report_dir = "outputs/reports"
    os.makedirs(dept_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)

    cleaned_rows = []
    with open(input_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            emp_id = row.get('employee_id', '').strip() or "UNKNOWN"
            emp_name = row.get('employee_name', '').strip() or "N/A"
            dept = row.get('department', '').strip() or "Chưa Phân Loại"
            date = row.get('record_date', '').strip()
            raw_status = row.get('task_status', '').strip()
            try:
                output_units = float(row.get('output_units', 0))
            except (ValueError, TypeError):
                output_units = 0.0

            if target_month and not date.startswith(target_month):
                continue

            cleaned_rows.append({
                'employee_id': emp_id,
                'employee_name': emp_name,
                'department': dept,
                'record_date': date,
                'output_units': output_units,
                'task_status': standardize_status(raw_status)
            })

    if not target_month:
        dates = [r['record_date'] for r in cleaned_rows if r['record_date']]
        month_str = sorted(dates)[-1][:7] if dates else datetime.now().strftime("%Y-%m")
    else:
        month_str = target_month

    # Group by department
    departments = sorted(list(set(r['department'] for r in cleaned_rows)))
    dept_stats = []

    for d in departments:
        d_rows = [r for r in cleaned_rows if r['department'] == d]
        slug_dept = slugify(d)
        dept_file = os.path.join(dept_dir, f"{slug_dept}_{month_str}.csv")

        with open(dept_file, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['employee_id', 'employee_name', 'department', 'record_date', 'output_units', 'task_status'])
            writer.writeheader()
            writer.writerows(d_rows)

        total_tasks = len(d_rows)
        done = len([r for r in d_rows if r['task_status'] == 'Completed'])
        in_prog = len([r for r in d_rows if r['task_status'] == 'In Progress'])
        delayed = len([r for r in d_rows if r['task_status'] == 'Delayed'])
        headcount = len(set(r['employee_id'] for r in d_rows))
        total_output = sum(r['output_units'] for r in d_rows)

        comp_rate = round((done / total_tasks * 100), 1) if total_tasks else 0.0
        delay_rate = round((delayed / total_tasks * 100), 1) if total_tasks else 0.0

        rating = "Normal (Healthy)"
        if delay_rate > 20:
            rating = "Red (High Risk)"
        elif delay_rate > 10:
            rating = "Yellow (Watchlist)"

        # Employee performance
        emp_dict = {}
        for r in d_rows:
            eid = r['employee_id']
            if eid not in emp_dict:
                emp_dict[eid] = {
                    'employee_id': eid,
                    'employee_name': r['employee_name'],
                    'total_tasks': 0,
                    'completed': 0,
                    'in_progress': 0,
                    'delayed': 0,
                    'output': 0.0
                }
            emp_dict[eid]['total_tasks'] += 1
            if r['task_status'] == 'Completed':
                emp_dict[eid]['completed'] += 1
            elif r['task_status'] == 'In Progress':
                emp_dict[eid]['in_progress'] += 1
            elif r['task_status'] == 'Delayed':
                emp_dict[eid]['delayed'] += 1
            emp_dict[eid]['output'] += r['output_units']

        emp_list = []
        for e in emp_dict.values():
            e['rate'] = round((e['completed'] / e['total_tasks'] * 100), 1) if e['total_tasks'] else 0.0
            emp_list.append(e)

        emp_list.sort(key=lambda x: (x['rate'], x['output']), reverse=True)

        dept_stats.append({
            'department': d,
            'slug': slug_dept,
            'headcount': headcount,
            'total_tasks': total_tasks,
            'completed': done,
            'in_progress': in_prog,
            'delayed': delayed,
            'completion_rate': comp_rate,
            'delay_rate': delay_rate,
            'total_output': total_output,
            'status_rating': rating,
            'file_path': dept_file,
            'employees': emp_list
        })

    total_tasks_comp = len(cleaned_rows)
    total_done_comp = len([r for r in cleaned_rows if r['task_status'] == 'Completed'])
    total_in_prog_comp = len([r for r in cleaned_rows if r['task_status'] == 'In Progress'])
    total_delayed_comp = len([r for r in cleaned_rows if r['task_status'] == 'Delayed'])
    total_headcount_comp = len(set(r['employee_id'] for r in cleaned_rows))
    total_output_comp = sum(r['output_units'] for r in cleaned_rows)

    comp_rate_all = round((total_done_comp / total_tasks_comp * 100), 1) if total_tasks_comp else 0.0
    delay_rate_all = round((total_delayed_comp / total_tasks_comp * 100), 1) if total_tasks_comp else 0.0

    best_dept = max(dept_stats, key=lambda x: x['completion_rate'])['department'] if dept_stats else "N/A"

    all_emps = []
    for d in dept_stats:
        for e in d['employees']:
            all_emps.append({
                'employee_id': e['employee_id'],
                'employee_name': e['employee_name'],
                'department': d['department'],
                'completed': e['completed'],
                'output': e['output'],
                'rate': e['rate']
            })
    top_3 = sorted(all_emps, key=lambda x: (x['output'], x['rate']), reverse=True)[:3]

    summary = {
        'month': month_str,
        'processed_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'total_headcount': total_headcount_comp,
        'total_tasks': total_tasks_comp,
        'total_completed': total_done_comp,
        'total_in_progress': total_in_prog_comp,
        'total_delayed': total_delayed_comp,
        'total_output': total_output_comp,
        'overall_completion_rate': comp_rate_all,
        'overall_delay_rate': delay_rate_all,
        'health_score': max(0, round(100 - (delay_rate_all * 2))),
        'best_department': best_dept,
        'top_performers': top_3,
        'departments': dept_stats
    }

    json_path = os.path.join(report_dir, "operations_kpi_summary.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=4)

    print(f"Processed {len(cleaned_rows)} records successfully.")
    print(f"Department files saved in {dept_dir}")
    print(f"Summary JSON saved in {json_path}")

if __name__ == '__main__':
    main()

# Alias entrypoint for app_lead_scoring.py
import sys
import os

# Delegate directly to app_lead_scoring
if __name__ == "__main__" or True:
    with open(os.path.join(os.path.dirname(__file__), "app_lead_scoring.py"), encoding="utf-8") as f:
        code = compile(f.read(), "app_lead_scoring.py", 'exec')
        exec(code, globals())

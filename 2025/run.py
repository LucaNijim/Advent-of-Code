# run.py
import importlib
import sys
from pathlib import Path

try:
    day = sys.argv[1]  # e.g. "01"
    module = importlib.import_module(f"solutions.day{day}")

    input_file = Path(f"input/day{day}").read_text().strip()
    print(module.solve(input_file))
except Exception as e:
    print(e)


import json
from pathlib import Path

 #---json read/write path---
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "data.json"

def load_json():

    #---check if file exists in file path
    if file_path.exists():
        with open(file_path, "r") as f:
            expenses = json.load(f)
        return expenses
    else:
        Expenses = dict[str, dict[str, dict[str, dict[str, object]]]]
        expenses: Expenses = {} # type: ignore
        return expenses


def save_json(expenses: dict)->None:

    with open(file_path, "w") as f:
            json.dump(expenses, f, indent=4)

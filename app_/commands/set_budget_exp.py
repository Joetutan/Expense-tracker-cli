from app_.infra.storage import load_json, save_json
from app_.infra.date_time import curr_month

def set_budget(amount:int) ->None:
    expenses = load_json()
    month = f'{curr_month()}'
    
    if expenses:
        expenses[month]["budget"] = amount
    else:
        expenses[month].setdefault("budget", 0)
        expenses[month]["budget"] = amount

    save_json(expenses)
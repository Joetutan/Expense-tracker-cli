
from app_.infra.date_time import curr_date, curr_month
from app_.infra.storage import load_json, save_json



def add(category: str,  description:str, amount: int ) -> None:

    expenses = load_json()

    #---genearte date instances---
    day = f'{curr_date()}'
    month = f'{curr_month()}'

    if not expenses:
        #---generate unique ID---
        task_id = 1
    elif month not in expenses:
        #---generate unique ID---
        task_id = 1
    elif day not in expenses[month]:
        #---generate unique ID---
        task_id = 1
    else:
        task_id = len(expenses[month][day])+1
         #---avoid duplicate IDs---
        while str(task_id) in expenses[month][day]:
                    task_id += 1

    #---create expense object---
    expenses.setdefault(month, {})
    expenses[month].setdefault(day, {})
    expenses[month].setdefault("total_expenses", 0)
    expenses[month].setdefault("budget", 0)
    expenses[month][day].setdefault(task_id,{})
    expenses[month][day][task_id]["category"] = category
    expenses[month][day][task_id]["description"] = description
    expenses[month][day][task_id]["amount"] = amount
    expenses[month]["total_expenses"] += amount
    

    save_json(expenses)
    
    print(f"Expense added successfully (ID: {task_id})")
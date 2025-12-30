
from app_.infra.date_time import curr_date, curr_month
from app_.infra.storage import load_json, save_json



def add(category: str,  description:str, amount: int ) -> None:

    # --- input validation ---
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if not category:
        raise ValueError("Category required")
    if not description:
         raise ValueError("Description required")

    expenses = load_json()

    #---generate date instances---
    day = f'{curr_date()}'
    month = f'{curr_month()}'

    #--- create unique expense id 
    if expenses:
        #---generate unique ID---
        task_id = len(expenses[month][day])+1
         #---avoid duplicate IDs---
        while str(task_id) in expenses[month][day]:
                    task_id += 1
    else:
        #---generate unique ID---
        task_id = 1
    

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
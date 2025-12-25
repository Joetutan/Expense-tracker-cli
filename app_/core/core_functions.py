from datetime import datetime
import json
from pathlib import Path
#from typing import Dict , Any

 #---json read/write path---
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "data.json"

def init_data_struct() -> dict:
    
    #---check if file exists in file path
    if file_path.exists():
        with open(file_path, "r") as f:
            expenses = json.load(f)
            
        return expenses
    else:
        Expenses = dict[str, dict[str, dict[str, dict[str, object]]]]
        expenses: Expenses = {} # type: ignore

        return expenses


def add_exp(category: str,  description:str, amount: int ) -> None:

    expenses = init_data_struct()

    #---genearte date instances---
    day = f'{datetime.now().strftime("%Y-%m-%d")}'
    month = f'{datetime.now().strftime("%Y-%m")}'

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
    expenses[month][day].setdefault(task_id,{})
    expenses[month][day][task_id]["category"] = category
    expenses[month][day][task_id]["description"] = description
    expenses[month][day][task_id]["amount"] = amount

    with open(file_path, "w") as f:
            json.dump(expenses, f, indent=4)
    
    print(f"Expense added successfully (ID: {task_id})")
    #print("ID.  Date          Category    description                   amount")
    #print(f"{task_id}.    {day}    {category}         {description}                  ${amount}")

def update_exp(id:int, description:str, amount: int, category: str) -> None:

    expense = init_data_struct()

    if expense:
         print()
    else:
         print()

def delete_exp(id:str)->None:
    print()

def list_exp(month_filter: int, date_filter: int)->None:
    expenses = init_data_struct()

    if expenses:
        if month_filter is None and date_filter is None:
                # --- Print all if no arguments parsed ---
                for k,v in expenses.items():
                    print(k)
                    for a,b in v.items():
                        print("  __________")
                        print(f"  {a}")
                        print("  __________")
                        print("  ID ---- Category ---- Description ---- Amount")
                        print("  _______________________________________________")
                        for ID in b:
                            category = expenses[k][a][ID]["category"]
                            description = expenses[k][a][ID]["description"]
                            amount = expenses[k][a][ID]["amount"]
                        
                            print(f"  {ID} ---- {category} ---- {description} ---- ${amount}")
        elif month_filter is not None and date_filter is None:
                #--- Print filter by month only
                for k,v in expenses.items():
                    print(k)
                    for a,b in v.items():
                        print("  __________")
                        print(f"  {a}")
                        print("  __________")
                        print("  ID ---- Category ---- Description ---- Amount")
                        print("  _______________________________________________")
                        for ID in b:
                            category = expenses[k][a][ID]["category"]
                            description = expenses[k][a][ID]["description"]
                            amount = expenses[k][a][ID]["amount"]
                        
                            print(f"  {ID} ---- {category} ---- {description} ---- ${amount}")
        else:
                # --- filter by month and date
                print()
                    
    else:
         print("No expenses in the books")
    
    print()

def set_budget(budget:int)->None:
    print()

def export_to_csv()->None:
     print()
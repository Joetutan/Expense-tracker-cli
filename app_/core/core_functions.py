from datetime import datetime
import json
from pathlib import Path

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
    day = f'{datetime.now().strftime("%d")}'
    month = f'{datetime.now().strftime("%m")}'

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
    expenses[month].setdefault("total_count", 0)
    expenses[month].setdefault("budget", 0)
    expenses[month][day].setdefault(task_id,{})
    expenses[month][day][task_id]["category"] = category
    expenses[month][day][task_id]["description"] = description
    expenses[month][day][task_id]["amount"] = amount
    expenses[month]["total_count"] += amount
    

    with open(file_path, "w") as f:
            json.dump(expenses, f, indent=4)
    
    print(f"Expense added successfully (ID: {task_id})")

def summary_exp(month:int )->None:
    expenses = init_data_struct()
    if expenses:
        running_total = expenses[str(month)]["total_count"]
        print(f"Total expenses: {running_total}")
    else: 
        print("No expenses in the books yet")

def list_exp(monthly_filter: int, date_filter: int)->None:

    expenses = init_data_struct()

    if expenses:

        if monthly_filter is None and date_filter is None:
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
                    

        elif monthly_filter is not None and date_filter is None:
                #--- Print filter by month only ---
                for k,v in expenses.items():
                    if k == str(monthly_filter):
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
                         continue
        elif monthly_filter is None and date_filter is not None:
                # --- filter by date ---
                for k,v in expenses.items():
                    print(k)
                    for a,b in v.items():
                        if a == str(date_filter):
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
            # --- filter by date and month ---
            for k,v in expenses.items():
                if k == str(monthly_filter):
                    for a,b in v.items():
                        if a == str(date_filter):
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
         print("No expenses in the books yet")

def update_exp(id:str, month: str , date: str, category: str, description:str, amount: int ) -> None:

    expenses = init_data_struct()

    if expenses:
        
        if id in expenses[month][date]:
                
                if category is not None:
                    expenses[month][date][id]["category"] = category
                elif description is not None:
                    expenses[month][date][id]["description"] = description
                elif amount is not None:
                    expenses[month][date][id]["amount"] = amount
            
                with open(file_path, "w") as f:
                    json.dump(expenses, f, indent=4)
    
                print(f"Expense updated successfully (ID: {id})")
            
    else:
        print("No expenses in the books yet")

def delete_exp(id:str, month: int, date: int)->None:
    expenses = init_data_struct()

    if expenses:
        if id in expenses[str(month)][str(date)]:

            amount = expenses[str(month)][str(date)][id]["amount"]
            expenses[month]["total_count"] -= amount

            expenses[str(month)][str(date)].pop(str(id))
            print(" # Expense deleted successfully")

            with open(file_path, "w") as f:
                    json.dump(expenses, f, indent=4)
        else:
            print("ID not found")
    else:
         print("No expenses in the books yet")



def export_to_csv()->None:
     print()
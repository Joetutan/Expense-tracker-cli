from app_.infra.storage import load_json
from app_.infra.date_time import curr_month

def summary(month:int )->None:
    #---input validation---
    if month is not None:
        if month <= 0:
            raise ValueError("Month must be positive value (1-31)")
    
    expenses = load_json()

   

    if expenses:
            if month is None:
                month_ = str(curr_month())
                running_total = expenses[month_]["total_expenses"]
                print(f"Total expenses: {running_total}")
            else:
                month_ = str(month)
                running_total = expenses[month_]["total_expenses"]
                print(f"Total expenses: {running_total}")
    else: 
            print("No expenses in the books yet")
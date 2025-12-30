from app_.infra.storage import load_json

def summary(month:int )->None:
    expenses = load_json()
    if expenses:
        running_total = expenses[str(month)]["total_expenses"]
        print(f"Total expenses: {running_total}")
    else: 
        print("No expenses in the books yet")
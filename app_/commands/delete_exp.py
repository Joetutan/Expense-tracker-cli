from app_.infra.storage import load_json, save_json




def delete(id:str, month: int, date: int)->None:
    expenses = load_json()

    if expenses:
        if id in expenses[str(month)][str(date)]:

            amount = expenses[str(month)][str(date)][id]["amount"]
            expenses[month]["total_expenses"] -= amount

            expenses[str(month)][str(date)].pop(str(id))
            print(" # Expense deleted successfully")

            save_json(expenses)

        else:
            print("ID not found")
    else:
         print("No expenses in the books yet")
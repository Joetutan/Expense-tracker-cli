from app_.infra.storage import load_json, save_json




def delete(id:int, month: int, date: int)->None:

    #--- input validation ---
    if id <= 0:
        raise ValueError(" ID must be positive value")
    elif month <= 0:
        raise ValueError(" Month must be positive value (1-12)")
    elif date <= 0:
        raise ValueError(" Date must be positive value (1-31)")
    
    expenses = load_json()

    id_ = str(id)
    month_ = str(month)
    date_ = str(date)

    if expenses:
        if id_ in expenses[month_][date_]:

            amount = expenses[month_][date_][id_]["amount"]
            expenses[month_]["total_expenses"] -= amount

            expenses[month_][date_].pop(id_)
            print(" # Expense deleted successfully")

            save_json(expenses)

        else:
            print("ID not found")
    else:
         print("No expenses in the books yet")
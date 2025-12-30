from app_.infra.storage import load_json, save_json


def update(id:int, month: int , date: int, category: str, description:str, amount: int ) -> None:

    #--- input validation ---
    if amount <= 0:
        raise ValueError(" Amount must be positive")
    elif id <= 0:
        raise ValueError(" ID must be positive value")
    elif month <= 0:
        raise ValueError(" Month must be positive value (1-12)")
    elif date <= 0:
        raise ValueError(" Date must be positive value (1-31)")
    

    expenses = load_json()

    id_ = str(id)
    date_ = str(date)
    month_ = str(month)

    if expenses:
        
        if id_ in expenses[month_][date_]:
                
                if category is not None:
                    expenses[month_][date_][id_]["category"] = category
                elif description is not None:
                    expenses[month_][date_][id_]["description"] = description
                elif amount is not None:
                    expenses[month_][date_][id_]["amount"] = amount
            
                save_json(expenses)
    
                print(f"Expense updated successfully (ID: {id_})")
        else:
            print(f"ID: {id_} not found")
            
    else:
        print("No expenses in the books yet")
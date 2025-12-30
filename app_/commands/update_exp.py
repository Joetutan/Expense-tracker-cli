from app_.infra.storage import load_json, save_json


def update_exp(id:str, month: str , date: str, category: str, description:str, amount: int ) -> None:

    expenses = load_json()

    if expenses:
        
        if id in expenses[month][date]:
                
                if category is not None:
                    expenses[month][date][id]["category"] = category
                elif description is not None:
                    expenses[month][date][id]["description"] = description
                elif amount is not None:
                    expenses[month][date][id]["amount"] = amount
            
                save_json(expenses)
    
                print(f"Expense updated successfully (ID: {id})")
            
    else:
        print("No expenses in the books yet")
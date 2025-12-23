from datetime import datetime
Expenses_data = {}


def add_exp(category: str,  description:str, amount: int ) -> None:
    #---generate unique ID---
    task_id = len(Expenses_data)+1
    #---genearte date item---
    time_stamp = f'{datetime.now().strftime("%Y-%m-%d")}'
    print("ID.  Date          Category    description                   amount")
    print(f"{task_id}.    {time_stamp}    {category}         {description}                  ${amount}")

def update_exp(id:int, description:str, amount: int, category: str) -> None:
    print()

def delete_exp(id:str)->None:
    print()

def list_exp(filter:str)->None:
    print()

def set_budget(budget:int)->None:
    print()
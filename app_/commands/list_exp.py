from app_.infra.storage import load_json

def list(monthly_filter: int, date_filter: int)->None:

    #--- positive integer validation ---
    if monthly_filter is not None:
        if monthly_filter <= 0:
            raise ValueError("Month must be positive integer (1-12)")
    if date_filter is not None:
        if date_filter <= 0:
            raise ValueError("Date must be positive integer (1-31)")

    expenses = load_json()

    if expenses:

        if monthly_filter is None and date_filter is None:
                # --- Print all if no arguments parsed ---
                for k,v in expenses.items():
                    print(k)
                    for a,b in v.items():

                        if a == "budget" or a == "total_expenses":
                            continue
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

                            if a == "budget" or a == "total_expenses":
                                continue

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

                        if a == "budget" or a == "total_expenses":
                            continue

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
                        
                        if a == "budget" or a == "total_expenses":
                            continue

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

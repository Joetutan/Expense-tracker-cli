Simple expense tracker application to manage your finances. The application should allow users to add, delete, and view their expenses. The application should also provide a summary of the expenses.

# Requirements
- Application should run from the command line and should have the following features:

- Users can add an expense with a description and amount.

- Users can update an expense.

- Users can delete an expense.

- Users can view all expenses.

- Users can view a summary of all expenses.

- Users can view a summary of expenses for a specific month (of current year).

## Additional features:

- Add expense categories and allow users to filter expenses by category.

- Allow users to set a budget for each month and show a warning when the user exceeds the budget.

- Allow users to export expenses to a CSV file.

- The list of commands and their expected output is shown below:

```bash
$ exp add --category Meals --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ exp add --category Meals --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ exp list --month 12 --date 30

#12
#  __________
#  30
#  __________
#  ID ---- Category ---- Description ---- Amount
#  _______________________________________________
#  1 ---- gym ---- monthly-subscription ---- $89.0
#  2 ---- gym ---- monthly-subscription ---- $89.0
#  3 ---- Meals ---- Lunch ---- $20.0
#  4 ---- Meals ---- Dinner ---- $10.0

$ exp summary
# Total expenses: $208.0

$ exp delete --id 2 --month 12 --date 30
# Expense deleted successfully

$ exp summary
# Total expenses: $119.0

$ expense-tracker summary --month 12
# Total expenses for December: $119.0

```
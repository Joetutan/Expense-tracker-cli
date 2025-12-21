Simple expense tracker application to manage your finances. The application should allow users to add, delete, and view their expenses. The application should also provide a summary of the expenses.

# Requirements
- Application should run from the command line and should have the following features:

- Users can add an expense with a description and amount.

- Users can update an expense.

- Users can delete an expense.

- Users can view all expenses.

- Users can view a summary of all expenses.

- Users can view a summary of expenses for a specific month (of current year).

## Additional features that you can add to the application:

- Add expense categories and allow users to filter expenses by category.

- Allow users to set a budget for each month and show a warning when the user exceeds the budget.

- Allow users to export expenses to a CSV file.

- The list of commands and their expected output is shown below:

```bash
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ expense-tracker summary
# Total expenses: $30

$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

$ expense-tracker summary --month 8
# Total expenses for August: $20

```
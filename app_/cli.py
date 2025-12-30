import argparse


def parse_arguments():
    
    parser = argparse.ArgumentParser(description="A simple cli expense tracker")

    subparsers = parser.add_subparsers(dest="command")

    # ---add expense---
    add_parser = subparsers.add_parser("add", help="add new expense")
    add_parser.add_argument("-c","--category", type=str,help="expense category")
    add_parser.add_argument("-d","--description", type=str , help="expense description")
    add_parser.add_argument("-a","--amount", type=float, help="amount spent")

    # --- list expense ---
    list_parser = subparsers.add_parser("list", help="list expenses [month, date]")
    list_parser.add_argument("-m","--month",default=None, type=int, choices=range(1, 13), metavar="MM",  help="Filter by month (1–12)")
    list_parser.add_argument("-d","--date", default=None, type=int, choices=range(1, 32), metavar="DD",  help="Filter by month (1–31)")

    # --- delete expense ---
    delete_parser = subparsers.add_parser("delete", help="delete expense (ID)")
    delete_parser.add_argument("--ID", type=int, help="expense ID")
    delete_parser.add_argument("--month", type=int, choices=range(1, 13), metavar="MM",  help="Filter by month (1–12)")
    delete_parser.add_argument("--date", type=int, choices=range(1, 32), metavar="DD",  help="Filter by month (1–31)")

    # --- update expense ---
    update_parser = subparsers.add_parser("update", help="Update expense (ID)")
    update_parser.add_argument("--ID", type=int, help="update expense ID")
    update_parser.add_argument("--month", type=int, choices=range(1, 13), metavar="MM",  help="Filter by month (1–12)")
    update_parser.add_argument("--date", type=int, choices=range(1, 32), metavar="DD",  help="Filter by month (1–31)")

    update_parser.add_argument("-c","--category", default=None, type=str,help="update expense category")
    update_parser.add_argument("-d","--description", default=None, type=str , help="update expense description")
    update_parser.add_argument("-a","--amount", default=None,type=float, help="update expense amount")

    # --- provide total expenses summary ---
    summary_parser = subparsers.add_parser("summary",  help="Total amount spent for the month")
    summary_parser.add_argument("-m","--month", type=int, choices=range(1, 13), metavar="MM",  help="Summary filtered by month (1–12)")
    
    # - set budget for current month ---
    set_budget_parser = subparsers.add_parser("budget", help="set budget for current month")
    set_budget_parser.add_argument("-b", "--budget", type=float, help="budget limit amount")


    return parser.parse_args()

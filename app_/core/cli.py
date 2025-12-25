import argparse
from app_.core.core_functions import add_exp,list_exp


def main() ->None:
    
    parser = argparse.ArgumentParser(description="A simple cli expense tracker")

    subparsers = parser.add_subparsers(dest="command")

    # ---add expense---
    add_parser = subparsers.add_parser("add", help="add new expense")
    add_parser.add_argument("category", type=str,help="expense category")
    add_parser.add_argument("description", type=str , help="expense description")
    add_parser.add_argument("amount", type=int, help="amount spent")

    # --- list expense ---
    list_parser = subparsers.add_parser("list", argument_default="all", help="list expenses [month, date]")
    list_parser.add_argument("-m","--month",default=None, type=int, choices=range(1, 13), metavar="MM",  help="Filter by month (1–12)")
    list_parser.add_argument("-d","--date", default=None, type=int, choices=range(1, 32), metavar="DD",  help="Filter by month (1–31)")


    args = parser.parse_args()

    match args.command:
        case "add":
            add_exp(args.category, args.description, args.amount)
        case "list":
            list_exp(args.month, args.date)
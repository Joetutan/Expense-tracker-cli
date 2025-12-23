import argparse
from app_.core.core_functions import add_exp


def main() ->None:
    
    parser = argparse.ArgumentParser(description="A simple cli expense tracker")

    subparsers = parser.add_subparsers(dest="command")

    # ---add expense---
    add_parser = subparsers.add_parser("add", help="add new expense")
    add_parser.add_argument("category", type=str,help="expense category")
    add_parser.add_argument("description", type=str , help="expense description")
    add_parser.add_argument("amount", type=int, help="amount spent")

    args = parser.parse_args()

    match args.command:
        case "add":
            add_exp(args.category, args.description, args.amount)
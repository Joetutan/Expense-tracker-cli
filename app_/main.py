from app_.cli import parse_arguments
from app_.core.core_functions import update_exp
from app_.commands.add_exp import add
from app_.commands.summary_exp import summary
from app_.commands.set_budget_exp import set_budget
from app_.commands.list_exp import list
from app_.commands.delete_exp import delete


def main():

    args = parse_arguments()

    match args.command:
        case "add":
            add(args.category, args.description, args.amount)
        case "list":
            list(args.month, args.date)
        case "update":
            if args.ID is None or  args.month is None or args.date is None:
                print(" --ID --month --date arguments needed for expense lookup.")
            else: 
                update_exp(str(args.ID), str(args.month), str(args.date), args.category, args.description, args.amount)
        case "delete":
            if args.ID is None or  args.month is None or args.date is None:
                print(" --ID --month --date arguments needed for expense lookup.")
            else:
                delete(args.ID, args.month, args. date)
        case "summary":
            summary(args.month)
        case "budget":
            set_budget(args.budget)

if __name__ == "__main__":
    main()

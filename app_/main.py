from app_.cli import parse_arguments
from app_.commands.add_exp import add
from app_.commands.summary_exp import summary
from app_.commands.set_budget_exp import set_budget
from app_.commands.list_exp import list
from app_.commands.delete_exp import delete
from app_.commands.update_exp import update


def main():

    args = parse_arguments()

    match args.command:
        case "add":
            add(args.category, args.description, args.amount)
        case "list":
            list(args.month, args.date)
        case "update":
                update(args.id, args.month, args.date, args.category, args.description, args.amount)
        case "delete":
                delete(args.id, args.month, args. date)
        case "summary":
            summary(args.month)
        case "budget":
            set_budget(args.budget)

if __name__ == "__main__":
    main()

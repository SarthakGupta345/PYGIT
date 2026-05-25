import argparse
import sys
print("Hello world")

def main():
    parser = argparse.ArgumentParser(
        description='Pygit A version controller to track version'
    )
    subparser = parser.add_subparsers(
        dest='Command' , help='Available commands'
    )

    init_parser = subparser.add_parser("init", help='Initialize a new repository')
    check_parser = subparser.add_parser("check", help='checking  a new repository')
    add_parser =     check_parser = subparser.add_parser("add", help='add  a new repository')


    args = parser.parse_args()
    print(args)
    
    if not args.Command:
        parser.print_help()
        return 
    
    try:
        if args.Command =='init':
            pass
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)


main()

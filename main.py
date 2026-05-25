import argparse
print("Hello world")

def main():
    parser = argparse.ArgumentParser(
        description='Pygit to track version'
    )
    subparser = parser.add_subparsers(
        dest='Command' , help='Available commands'
    )

    init_parser = subparser.add_parser("init", help='Initialize a new repository')
    check_parser = subparser.add_parser("check", help='checking  a new repository')

    args = parser.parse_args()
    print(args)

main()

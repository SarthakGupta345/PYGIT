import argparse
from pathlib import Path
import sys
print("Hello world")

class Repository:
    def __init__(self,path='.') -> None:
        self.path = Path(path).resolve()
        self.git_dir = self.path/".pygit"

        self.object_dir = self.git_dir/'objects'
        self.ref_dir = self.git_dir/'refs'
        self.head_dir = self.git_dir/'HEAD'

        self.index_file = self.git_dir/'index'

    def init(self)-> bool:
        # directories
        self.git_dir.mkdir()
        self.object_dir.mkdir()
        self.ref_dir.mkdir()

        return True


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

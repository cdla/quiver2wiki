import os
import sys
import argparse

def main():

    parser = argparse.ArgumentParser(
    description = 'helper tool for making quiver libraries into wikis')

    parser.add_argument("--export",dest='export', help="export quiver library into markdown files", type=str, default=None)
#    parser.add_argument("--host",dest='host',
#    help="host the wiki formed from the quiver library", type=str, default=None)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    if args.export != None:
        export2md(args.export)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

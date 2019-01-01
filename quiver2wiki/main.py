import os
import sys
import argparse
from quiver2wiki.scripts import export2md
from quiver2wiki.scripts import utils

def main():

    parser = argparse.ArgumentParser(
    description = 'helper tool for making quiver libraries into wikis')
    parser.add_argument("quiver_lib", type=str, help = "location of the quiver library")
    parser.add_argument("--list",dest='list', help="lists the quiver notebooks", default=False, action='store_true')
    parser.add_argument("--list_pages",dest='list_pages', help=" lists the quiver notebooks and pages", default=False, action='store_true')
    parser.add_argument("--export",dest='export', help="export quiver library into markdown files", type=str, default=None)

#    parser.add_argument("--host",dest='host',
#    help="host the wiki formed from the quiver library", type=str, default=None)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    if args.list == True:
        nb_list=utils.list_notebooks(args.quiver_lib)
        print("The list of notebooks within the quiver library at %s is: "%(args.quiver_lib))
        for nb in nb_list:
            print(nb)
    elif args.export != None:
        export2md(args.export)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

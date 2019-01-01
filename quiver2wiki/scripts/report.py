import os


def report_notebooks(quiver_lib,nb_list):
    print("The list of notebooks within the quiver library at %s is: "%(quiver_lib))
    for nb in nb_list:
        print(nb)

def report_pages(quiver_lib,page_dict):
    print("The page organization for the quiver library at %s is: "%quiver_lib)

    for page in page_dict:
        print("Quiver Notebook: %s"%page)
        if len(page_dict[page]) == 0:
            print("    There are no pages within this notebook")
        else:
            for page in page_dict[page]:
                print("    - %s "%page)

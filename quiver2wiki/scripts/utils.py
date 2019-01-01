import os
from glob import glob
import json

def list_notebooks(quiver_location,private_list=[]):
    ''' list_notebooks will return a list of the notebooks, ignoring the private notebooks
    :param quiver_location: the location of the quiver library of notebooks
    :param private_list: the list of private notebooks to ignore

    TODO: add ignore private_list functionality
    '''
    meta_json = os.path.join(quiver_location,'meta.json')

    nb_meta_jsons=glob(os.path.join(quiver_location,'*','meta.json'))
    nb_list = []
    nb_dict = dict()
    for nb_meta_json in nb_meta_jsons:
        with open(nb_meta_json,'r') as meta_file:
            meta = json.load(meta_file)
            nb_list.append(meta['name'])
            nb_dict[meta['name']]=meta
    return nb_list,nb_dict

def list_pages(quiver_location,nb_dict, private_list=[]):
    ''' list_pages will return a list of pages of the notebooks, ignoring the private notebooks
    :param quiver_location: the location of the quiver library of notebooks
    :param nb_dict: a dictionary of the quiver notebooks within the library
    :param private_list: the list of private notebooks to ignore

    TODO: add ignore private_list functionality
    TODO: add function for further recursive notebooks
    '''

    nb_page_dict=dict()

    for nb in nb_dict:
        nb_page_list=dict()

        nb_page_list[nb_dict[nb]['name']]=[]
        page_meta_jsons=glob(os.path.join(quiver_location,nb_dict[nb]['uuid'] + ".qvnotebook",'*','meta.json'))

        for page_meta_json in page_meta_jsons:
            with open(page_meta_json,'r') as meta_file:
                meta = json.load(meta_file)
                nb_page_list[nb_dict[nb]['name']].append(meta['title'])

        nb_page_dict[nb] = sorted(nb_page_list[nb])

    return nb_page_dict

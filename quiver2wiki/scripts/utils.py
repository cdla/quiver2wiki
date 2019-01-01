import os
from glob import glob
import json

def list_notebooks(quiver_location,private_list=[]):
    ''' list_notebooks will return a list of the notebooks, ignoring the private notebooks
    :param quiver_location: the location of the quiver library of notebooks
    :param private_list: the list of private notebooks to ignore
    '''
    meta_json = os.path.join(quiver_location,'meta.json')

    nb_meta_jsons=glob(os.path.join(quiver_location,'*','meta.json'))
    nb_list = []
    for nb_meta_json in nb_meta_jsons:
        with open(nb_meta_json,'r') as meta_file:
            meta = json.load(meta_file)
            nb_list.append(meta['name'])

    return nb_list

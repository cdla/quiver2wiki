import os
from glob import glob
import markdown
import json

def get_overall_structure(quiver_location,ignore_notebooks=[]):
    ''' get_overall_structure will return the overall structure for the quiver library of notebooks

    TODO: ignore private libraries
    '''

    meta_json = os.path.join(quiver_location,'meta.json')
    meta = json.loads(meta_json)

    notebooks = glob(os.path.join(quiver_location,"*qvnotebook",""))
    notebooks_to_remove=ignore_notebooks.append('Trash.qvnotebook')

    notes=dict()
    for notebook in notebooks:
        notes{notebook} = json.load(os.path.join(notebooks,"meta.json"))
        notes{notebook}['file_location'] = notebook

    overall_structure = notes

    return overall_structure

def load_pages(quiver_location,overall_structure):

    pages = dict()

    for notebook in overall_structure.keys():
        pages{notebook}
        pages{notebook}['meta']=
    return

def batch_export(quiver_location,wiki_location,overall_structure,pages):
    ''' batch_export takes the overall structure of the notebook, and creates a dictionary of pages to export, and then exports the pages into markdown for wiki hosting
    '''


    return

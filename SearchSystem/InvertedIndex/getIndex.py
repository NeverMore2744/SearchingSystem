import json
import tools
from . import invertedIndex

def get_index():
    idx = invertedIndex.InvertedIndex(_doc_path="/InvertedIndex/Reuters", _get_item_list=invertedIndex._test_get_item_list)
    index = idx.get_index()
    return index

get_index()
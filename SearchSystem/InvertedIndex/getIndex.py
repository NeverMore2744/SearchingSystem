import json
import tools
from . import invertedIndex

def get_inverted_index():
    idx = invertedIndex.InvertedIndex(_doc_path="/InvertedIndex/Reuters", _get_item_list=invertedIndex._test_get_item_list)
    return idx

def get_index():
    idx = invertedIndex.InvertedIndex(_doc_path="/InvertedIndex/Reuters", _get_item_list=invertedIndex._test_get_item_list)
    index = idx.get_index()
    return index

# get_inverted_index()
# get_index()

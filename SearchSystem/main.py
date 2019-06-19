import os
import tools
import nltk
from InvertedIndex import getIndex
from LanguageAnalysis import stemming
from Serching import searchWord
from BoolSearch import BoolSearchDel

print("The first time to load this System?[Y]/[N] ", end='')
choose = input()
if choose == "Y":
    nltk.download("wordnet")
    nltk.download("averaged_perceptron_tagger")
    nltk.download("punkt")
    nltk.download("maxnet_treebank_pos_tagger")

print("getting index...")
INVERTED_INDEX = getIndex.get_inverted_index()
INDEX = INVERTED_INDEX.get_index()
DOC_NUM = INVERTED_INDEX.get_doc_num()

#print(INDEX)

# print("loading the wordnet...")
# stemming.lemmatize_sentence("a", False)

LOOP = True
print("=================Searching System=================")
SEARCH_NUM=1

K=10

while LOOP:
    print("---------> Start search No. {0}".format(SEARCH_NUM))
    syn_FLAG = False

    print("Enable Synonym Retrieval?[Y]/[N] ", end='')
    choose = input()
    if choose == "Y":
        syn_FLAG = True 

    print("input the query statement(EXIT to quit): ", end='')
    STATEMENT = input()
    if STATEMENT == "EXIT":
        break

    print("stemming...")
    INPUT_WORDS = stemming.lemmatize_sentence(STATEMENT, True)

    DOC_LIST = BoolSearchDel.bool_search(DOC_NUM, INPUT_WORDS, INDEX, syn_FLAG)
    
    print("Found {0} document(s)  that matched query".format(len(DOC_LIST)))
    for i in range(min(K, len(DOC_LIST))):
        print("doc name:{0}.html, score = {1}".format(DOC_LIST[i][0], DOC_LIST[i][1]))

    SEARCH_NUM += 1

print("ByeBye!")

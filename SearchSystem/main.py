import os
import tools
import nltk
from InvertedIndex import getIndex
from LanguageAnalysis import stemming
from Serching import searchWord
from BoolSearch import BoolSearchDel

print("The first time to load this System?[Y]/[N]")
choose = input()
if choose == "Y":
    nltk.download("wordnet")
    nltk.download("averaged_perceptron_tagger")
    nltk.download("punkt")
    nltk.download("maxnet_treebank_pos_tagger")

print("getting index...")
INDEX = getIndex.get_index()
#print(INDEX)

print("loading the wordnet...")
stemming.lemmatize_sentence("a", False)

LOOP = True
print("=================Searching System=================")

while LOOP:
    print("input the query statement(EXIT to quit):")
    STATEMENT = input()
    if STATEMENT == "EXIT":
        break

    print("stemming...")
    INPUT_WORDS = stemming.lemmatize_sentence(STATEMENT, True)
    print(INPUT_WORDS)

    DOC_LIST = BoolSearchDel.bool_search(INPUT_WORDS, INDEX)
    print(len(DOC_LIST), "DOCs :")
    print(DOC_LIST)

print("ByeBye!")

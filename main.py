# An automatic summarizer.
# Kirsten Vail, Derek Palinski, and Lee Schumann

from nltk.corpus import reuters
from nltk.corpus import stopwords as swCorpus
import math

'''
A function to sort a dictionary.
Author: Derek Palinski
'''
def sortDict(weights):
    ret = [(weights[key], key) for key in weights]
    ret.sort()
    ret.reverse()
    return ret

def getPosition(tup):
    return tup[1]

# count how many documents the word appears in
docCounts = {}
for fid in reuters.fileids():
    docWords = set()
    for word in reuters.words(fid):
        word = word.lower()
        if word not in docWords:
            docWords.add(word)
            if word in docCounts.keys():
                docCounts[word] += 1
            else:
                docCounts[word] = 1

# get a set of the stopwords to ignore in creating the weights.
swList = swCorpus.words('english')
stopwords = set(swList)

# create a count for all the words in the article
inCount = {}
for word in reuters.words('test/14862'):
    word = word.lower()  # generalize by making them all lowercase
    if word not in stopwords and word.isalpha():
        if word in inCount.keys():
            inCount[word] += 1
        else:
            inCount[word] = 1

# Create a weighting for each word in the article
weights = {}
size = len(reuters.fileids())
for word in inCount.keys():
    weights[word] = inCount[word] * math.log(size / docCounts[word])

# print the words in the article with their weights
for tup in sortDict(weights):
    print(tup[1] + ' ' + str(tup[0]))

#get sentence weights and keep the top 20 ones.
length = 10
impSents = []
for index, sentence in enumerate(reuters.sents('test/14862')):
    sentWeight = 0
    for word in sentence:
        word = word.lower()
        if word in weights.keys():
            sentWeight += weights[word]

    if len(impSents) < length or sentWeight > impSents[length-1][0]:
        tup = (sentWeight, index, sentence)
        impSents.append(tup)
        impSents.sort()
        if len(impSents) > length:
            impSents = impSents[:(length-1)]
print()
print(reuters.raw('test/14862'))
print()
impSents.sort(key=getPosition)
for tup in impSents:
    sentence = tup[2]
    for word in sentence:
        print(word, end=' ')
    print()
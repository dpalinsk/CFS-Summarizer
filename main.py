from nltk.corpus import reuters
from nltk.corpus import stopwords as swCorpus
import math

#count how many documents the word appears in
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

#create a count for all the words in the article
inCount = {}
for word in reuters.words('test/14862'):
    word = word.lower()  # generalize by making them all lowercase
    if word not in stopwords:
        if word in inCount.keys():
            inCount[word] += 1
        else:
            inCount[word] = 1

#Create a weighting for each word in the article
weights = {}
size = len(reuters.fileids())
for word in inCount.keys():
    weights[word] = inCount[word] * math.log(size/docCounts[word])

#print the words in the article with their weights
for word in weights.keys():
    print(word + ' ' + str(weights[word]))

#TODO
    # add up weights to create weighting for sentences
    # select certain sentences for the summary
    # See what happens!
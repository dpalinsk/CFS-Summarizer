# An automatic summarizer.
# Kirsten Vail, Derek Palinski, and Lee Schumann

from nltk.corpus import reuters
from nltk.corpus import stopwords as swCorpus
import math

'''
A class for our summarizer object
'''


class Summarizer:

    def __init__(self):
        # get the counts of how many documents each word appears in
        self.docCounts = self.getDocCounts()
        # get a set of the stopwords to ignore in creating the weights.
        swList = swCorpus.words('english')
        self.stopwords = set(swList)

    '''
    A function to count how many times various words appear.
    '''

    def getDocCounts(self):
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
        return docCounts

    '''
    Summarize and print the text
    '''

    def summarize(self, article, length):
        # get the weights for each word in the focus document and print them
        weights = self.getWordWeights(article)
        #self.printWeights(weights)

        # get the important sentences and print them
        impSents = self.getSentences(weights, article, length)
        sentList = self.getList(impSents)

        #print()
        #self.printSents(impSents)

        return sentList

    '''
    Get the weight of each unique word, based on a simple tf-idf scheme.
    '''

    def getWordWeights(self, article):
        # get the counts of all the the number of times each word appears within the article
        inCount = self.getWordCounts(article)

        # weight each non-stop word
        weights = {}
        size = len(reuters.fileids())
        for word in inCount.keys():
            weights[word] = inCount[word] * math.log(size / self.docCounts[word])

        return weights

    '''
    A function to count the number of times each non-stop word in the article appears
    within that article.
    '''

    def getWordCounts(self, article):
        # create a count for all the words in the article
        inCount = {}
        for word in reuters.words(article):
            word = word.lower()  # generalize by making them all lowercase
            if word not in self.stopwords and word.isalpha():
                if word in inCount.keys():
                    inCount[word] += 1
                else:
                    inCount[word] = 1
        return inCount

    '''
    A function which prints the weights of all the words in the focus document in decending order
    '''

    def printWeights(self, weights):
        for tup in self.sortDict(weights):
            print(tup[1] + ' ' + str(tup[0]))

    '''
    A function to sort a dictionary.
    Author: Derek Palinski
    '''

    def sortDict(self, weights):
        ret = [(weights[key], key) for key in weights]
        ret.sort()
        ret.reverse()
        return ret

    '''
    A function which returns the sentences of sufficient weight for a given length in the order of their appearance.
    '''

    def getSentences(self, weights, article, length):
        impSents = []
        for index, sentence in enumerate(reuters.sents(article)):
            # calculate the weight of the sentence
            sentWeight = 0
            for word in sentence:
                word = word.lower()
                if word in weights.keys():
                    sentWeight += weights[word]

            # add the sentence if it is above the least weighted sentence in the list
            if len(impSents) < length or sentWeight > impSents[length - 1][0]:
                tup = (sentWeight, index, sentence)
                impSents.append(tup)
                impSents.sort(reverse=True)
                if len(impSents) > length:
                    impSents = impSents[:(length - 1)]

        impSents.sort(key=self.getPosition)
        return impSents

    '''
    A function which serves as the key to sorting the final selected sentences.
    '''

    def getPosition(self, tup):
        return tup[1]

    '''
    A function which returns just a list of sentences in the summary
    '''
    def getList(self, impSents):
        list = []
        for sent in impSents:
            sentence = sent[2]
            list.append(sentence)
        return list

    '''
    A function which prints each sentence
    '''
    def printSents(self, impSents):
        # TODO
        # add more stuff which would allow it to print the sentence more naturally
        for tup in impSents:
            sentence = tup[2]
            for word in sentence:
                print(word, end=' ')
            print()
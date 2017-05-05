# An automatic summarizer.
# Kirsten Vail, Derek Palinski, and Lee Schumann

from nltk.corpus import reuters
from nltk.corpus import stopwords as swCorpus
from position import position
import math
import paragraphs

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
    Summarize the text and return the sentences in the form of a list of lists of words
    '''
    def summarize(self, article, length):
        # get the important sentences and print them
        important_sentences = self.getSentences(article, length)
        sentence_list = self.getList(important_sentences)
        return sentence_list

    '''
    A function which returns the sentences of sufficient weight for a given length in the order of their appearance.
    '''
    def getSentences(self, article, length):
        # get the weights for each word in the focus document and print them
        word_weights = self.getWordWeights(article)

        sentence_index = 0
        #important_sentences = []

        paragraphs_tokenized = paragraphs.para_tokenize(reuters.raw(article))
        position_weighted_sentences = position(paragraphs_tokenized)
        word_weighted_sentences = []
        for paragraph_index, paragraph in enumerate(paragraphs_tokenized):
            for sentence in paragraph:
                # calculate the weight of the sentence
                #The heuristics:
                sum_word_weight = self.getSumofWordWeights(sentence, word_weights)
                position_weight = 0
                #............
                #Add them together with multipliers:
                sentence_weight = 1*sum_word_weight + 1*position_weight
                #add sentence to list
                tup = (sentence_weight, sentence_index, sentence)
                word_weighted_sentences.append(tup)

                '''
                # add the sentence if it is above the least weighted sentence in the list
                if len(important_sentences) < length or sentence_weight > important_sentences[length - 1][0]:
                    #store the sentence as a tuple with the sentence weight,
                    tup = (sentence_weight, sentence_index, sentence)
                    important_sentences.append(tup)
                    important_sentences.sort(reverse=True)
                    if len(important_sentences) > length:
                        important_sentences = important_sentences[:(length - 1)]
                '''

                sentence_index += 1

        #combine the heuristics
        important_sentences = []
        sentence_index = 0
        for paragraph in paragraphs_tokenized:
            for sentence in paragraph:
                sum_word_weight = word_weighted_sentences[sentence_index][0]
                position_weight = position_weighted_sentences[sentence_index][0]

                print(sum_word_weight)
                print(position_weight)

                sentence_weight = 1*sum_word_weight + 100*position_weight
                tup = (sentence_weight, sentence_index, sentence)
                important_sentences.append(tup)

                sentence_index += 1

        #clip the number of sentences
        important_sentences.sort(key=self.getPosition)
        important_sentences = important_sentences[:(length - 1)]

        important_sentences.sort(key=self.getPosition)
        return important_sentences

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
    A function which gets the sum of the word weights in the sentence
    '''
    def getSumofWordWeights(self, sentence, word_weights):
        sum_word_weight = 0
        for word in sentence:
            word = word.lower()
            if word in word_weights.keys():
                sum_word_weight += word_weights[word]
        return sum_word_weight

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
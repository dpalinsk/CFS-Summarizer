"""
Scanner.py
Reads in input and stores word counts
@dpalinsk
10 Apr 2017
"""
from sys import argv
import string 
filename = argv[1]
txt = open(filename, 'r')
stopwords = open("stopwords.txt", 'r')
freqs = {}
stops = []

def buildStopWordList(file):
	for line in file:
		for word in line.split():
			stops.append(word);

def containsNumber(str):
	return any(char.isdigit() for char in str);

def countFrequencies(file):
	exclude = str.maketrans("", "", string.punctuation)
	for line in file:
		for word in line.split():
			word = word.translate(exclude).lower()
			if word in freqs:
				freqs[word] += 1
			else:
				if word != '' and word not in stops and not containsNumber(word) and len(word) > 1:
					freqs[word] = 1

def sortDict(freqs):
	ret = [(freqs[key],key) for key in freqs];
	ret.sort();
	ret.reverse();
	return ret;

buildStopWordList(stopwords)
countFrequencies(txt);
print(sortDict(freqs)) 
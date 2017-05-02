from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import punkt
import nltk.data

'''
This function returns the paragraphs in the form of a list of sentences, which are a list of words.
The function accepts the string form of the raw text from the corpus.
The function uses exactly the same sentence and word tokenizer as the NLTK rawtext copus reader.
'''
def para_tokenize(text):
    #get the rawtext corpus tokenizers to tokenize this after we have the paragraphs
    word_tokenizer = WordPunctTokenizer()
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    #make sure we're working with a string so we can use string methods
    if type(text) != str:
        text = str(text)
    string = text

    string = string.replace('\n', '')
    raw_paragraphs = string.split('      ')

    full_tokenized = []
    for raw_para in raw_paragraphs:
        tokenized_para = []
        sentences = sent_tokenizer.tokenize(raw_para)
        for sent in sentences:
            tokenized_para.append(word_tokenizer.tokenize(sent))
        full_tokenized.append(tokenized_para)

    return full_tokenized

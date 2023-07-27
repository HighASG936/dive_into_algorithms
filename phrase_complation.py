from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.util import ngrams
import requests
from collections import Counter
import numpy as np


def get_corpus(url):
    """
    Download corpus and return a string from the text
    """
    file = requests.get(url)
    file = file.text    
    text = file.replace('\n', '')    
    return text


def tokenizing(text):
    """
    Tokenize the text and return and array with each n-gram
    tokens
    """
    global grams
    
    try:
        token = nltk.word_tokenize(text)    
    except LookupError:
        nltk.download('punkt')
        tokenizing(text)
    else:
        for n in range(2, 6):
            grams.append(ngrams(token, n))


def finding_candidate(search_term):
    """
    Finding candidate n + 1-grams
    """
    global grams
    
    split_term = tuple(search_term.split(' '))
    search_term_length = len(search_term.split(' '))
    counted_grams = Counter(grams[search_term_length - 1])    
    matching_terms = [element for element in list(counted_grams.items()) \
                                if element[0][:-1] == tuple(split_term)]
    
    return matching_terms


def selecting_a_phrase(matching_terms):
    """
    Selecting a phrase based on frequency
    """
    if len(matching_terms) > 0:
        frequencies = [item[1] for item in matching_terms]
        maximum_frequency = np.max(frequencies)
        highest_frequency = [item[0] for item in matching_terms \
                             if item[1] == maximum_frequency][0]
        combined_term = ' '.join(highest_frequency)
    return combined_term


def search_suggestions(search_term , text):
    """
    Integration of all functions to realize the phrase complation
    """
    tokenizing(text)
    matching_terms = finding_candidate(search_term)
    combined_term = selecting_a_phrase(matching_terms)
    return combined_term


if __name__ == '__main__':  
    grams = []
    url_corpus = 'http://www.bradfordtuckfield.com/shakespeare.txt'  
    search_term = 'life is a'
    text = get_corpus(url_corpus)
    print(search_suggestions(search_term , text))
    

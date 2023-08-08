import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial
import numpy as np
import nltk, string

def remove_punctuation_map():
    """
    
    """
    return dict((ord(char), None) for char in string.punctuation)

def remove_punctuation_lowercase_query(query):
    """
    
    """
    query_lowercase = query.lower()
    return query_lowercase.translate(remove_punctuation_map())

def tokenize(query):
    """
    
    """
    translated_query = remove_punctuation_lowercase_query(query)
    return nltk.word_tokenize(translated_query)

def stem_tokens(tokens):
    """
    
    """
    stemmer = nltk.stem.PorterStemmer()
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    """
    
    """
    return stem_tokens(tokenize(text))

if __name__ == '__main__':
    query = 'I want to learn about geometry algorithms.'
    print(normalize(query))

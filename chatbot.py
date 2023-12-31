import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial
import numpy as np
import nltk, string
import warnings

warnings.filterwarnings("ignore", category=UserWarning, message='')

def remove_punctuation_map():
    """
    
    """
    return dict((ord(char), None) for char in string.punctuation)

def remove_punctuation_lowercase_query(query):
    """
    
    """
    query_lowercase = query.lower()
    return query_lowercase.translate(remove_punctuation_map())

def get_word_tokenize(translated_query):
    """
    
    """
    try:
        return nltk.word_tokenize(translated_query)
    except LookupError:
        nltk.download('punkt')
        return get_word_tokenize()

def tokenize(query):
    """
    
    """
    translated_query = remove_punctuation_lowercase_query(query)
    return get_word_tokenize(translated_query)

def stem_tokens(tokens):
    """
    
    """
    stemmer = nltk.stem.porter.PorterStemmer()
    return [stemmer.stem(item) for item in tokens]

def normalize(query):
    """
    
    """
    return stem_tokens(tokenize(query))

def text_vectorization(query, alldocuments):
    """
    
    """
    vctrz = TfidfVectorizer(ngram_range=(1,1), tokenizer=normalize, stop_words='english')
    vctrz.fit(alldocuments)
    tfidf_reports = vctrz.transform(alldocuments).todense()
    tfidf_question = vctrz.transform([query]).todense()
    
    return tfidf_reports, tfidf_question

def vector_similarity(tfidf_reports, tfidf_question):
    """
    
    """
    row_similarities = [1 - spatial.distance.cosine(np.ravel(tfidf_reports[x]), np.ravel(tfidf_question)) \
                        for x in range(len(tfidf_reports))]
    return row_similarities

def chatbot(query, alldocuments):
    """    
    
    """
    tfidf_reports, tfidf_question = text_vectorization(query, alldocuments)
    
    row_similatiries = vector_similarity(tfidf_reports, tfidf_question)
    
    return alldocuments[np.argmax(row_similatiries)]

if __name__ == '__main__':
    query = 'I want to learn about magic squares.'
    alldocuments = [
                    'Chapter 1. The algorithmic approach to problem solving, including Galileo and baseball.', 
                    'Chapter 2. Algorithms in history, including magic squares, Russian peasant multiplication, and Egyptian methods.', 
                    'Chapter 3. Optimization, including maximization, minimization, and the gradient ascent algorithm.', 
                    'Chapter 4. Sorting and searching, including merge sort, and algorithm runtime.', 
                    'Chapter 5. Pure math, including algorithms for continued fractions and random numbers and other mathematical ideas.', 
                    'Chapter 6. More advanced optimization, including simulated annealing and how to use it to solve the traveling salesman problem.',
                    'Chapter 7. Geometry, the postmaster problem, and Voronoi triangulations.',
                    'Chapter 8. Language, including how to insert spaces and predict phrase completions.',
                    'Chapter 9. Machine learning, focused on decision trees and how to predict happiness and heart attacks.',
                    'Chapter 10. Artificial intelligence, and using the minimax algorithm to win at dots and boxes.',
                    'Chapter 11. Where to go and what to study next, and how to build a chatbot.',
                    ]

    print(chatbot(query, alldocuments))

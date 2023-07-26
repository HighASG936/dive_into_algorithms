import re
import nltk
from nltk.corpus import brown
import numpy as np

text = "The oneperfectly divine thing, the oneglimpse of God's paradisegiven on earth, is to fight a losingbattle - and notlose it."    

def remove_special_chars(word_list):
    """Return a new word_list without special characters"""
    special_characters = ['*', '[', ']', '?', '.', '+', '/', ';', ':', ',', \
                          ')', '(']
    for sp in special_characters:
        word_list = [word.replace(sp, '') for word in word_list]
    word_list.remove('')
    return word_list
 
 
def get_corpus(corpus):
    """
    Download corpus and find the spaces that are not valid by using an imported
    corpus to check valid words and return this new modified list
    """
    try:
        return remove_special_chars(list(set(brown.words())))
    except LookupError:
        nltk.download(corpus)
        return get_corpus(corpus)


def get_spaces_starts_positions(text):
    """
    Get positions of spaces from 'text'.
    Return a list with this positions inside.
    """    
    spacestarts = [m.start() for m in re.finditer(' ', text)]
    spacestarts.append(-1)
    spacestarts.append(len(text))
    spacestarts.sort()
    spacestarts_affine = [ss + 1 for ss in spacestarts]
    spacestarts_affine.sort()
    return spacestarts, spacestarts_affine


def get_first_partial_words_positions(locs, spacestarts, spacestarts_affine):
    """Get first partial words positions from suspected word"""
    return [
            loc for loc in locs \
            if loc[0] in spacestarts_affine and loc[1] not in spacestarts
           ]


def get_last_partial_words_positions(locs, spacestarts, spacestarts_affine):
    """Get last partial words positions from suspected word"""
    return [
            loc for loc in locs \
            if loc[0] not in spacestarts_affine and loc[1] in spacestarts
           ]


def get_between_spaces(locs, spacestarts, spacestarts_affine):
    """
    Get all the substrings that are between two spaces & find the spaces
    that are not valid and return them
    """
    between_spaces = [(spacestarts[k] +1, spacestarts[k+1]) \
                      for k in range(0, len(spacestarts) -1)]
    between_spaces_notvalid = [loc for loc in between_spaces \
                               if text[loc[0]:loc[1]] not in word_list]
    return between_spaces, between_spaces_notvalid


def get_new_text(text, partial_words, partial_words_end, between_spaces_notvalid):
    """ """
    textnew = text    
    for loc in between_spaces_notvalid:
        endsofbeginnings = [loc2[1] for loc2 in partial_words \
                            if loc2[0] == loc[0] and (loc2[1] - loc[0]) > 1]
        
        beginningsofends = [loc2[0] for loc2 in partial_words_end \
                            if loc2[1] == loc[1] and (loc2[1] - loc[0]) > 1]        
        pivot = list(set(endsofbeginnings).intersection(beginningsofends))
        if len(pivot) > 0:
            pivot = np.min(pivot)
            textnew = textnew.replace(text[loc[0]:loc[1]],
                                      text[loc[0]:pivot]+' '+text[pivot:loc[1]])
    textnew = textnew.replace('  ', ' ')
    return textnew


def insertspaces(text, word_list):
    """ """    
    #Get start and end positions for each word from 'text' that
    #are in 'word_list'
    locs = list(set([(m.start(), m.end()) \
                     for word in word_list \
                     for m in re.finditer(word, text)]
                    )
                )
    
    #Get start positions for each spaces in 'word_list'
    spacestarts, spacestarts_affine = get_spaces_starts_positions(text)
    
    #Check in word_list for words that could be combined to from those invalid
    #words
    partial_words = get_first_partial_words_positions(locs, spacestarts,
                                                      spacestarts_affine)
    partial_words_end = get_last_partial_words_positions(locs, spacestarts,
                                                         spacestarts_affine)

    #Get all the substrings that are between two spaces & find the spaces that
    #are not valid
    between_spaces, between_spaces_notvalid = get_between_spaces(
                                                             locs,
                                                             spacestarts,
                                                             spacestarts_affine)
    
    return get_new_text(text, partial_words, partial_words_end, between_spaces_notvalid)


if __name__ == '__main__':
    word_list = get_corpus('brown')        
    print(insertspaces(text, word_list))


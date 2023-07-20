import re
import nltk
from nltk.corpus import brown


if __name__ == '__main__':
    text = "The oneperfectly divine thing, the oneglimpse of God's paradisegiven on earth, is to fight a losingbattle - and notlose it."
    word_list = ['The', 'one', 'perfectly', 'divine']
    special_characters = ['*', '[', ']', '?', '.', '+', '/', ';', ':', ',', \
                          ')', '(']

    nltk.download('brown')

    #Find words with 'n'
    has_n = [word for word in word_list if 'n' in word]
    print(has_n)

    #Get start and end positions for each word from 'text' that are in 'word_list'
    locs = list(set([ (m.start(), m.end()) \
                       for word in word_list \
                       for m in re.finditer(word, text) ]))
    print(locs)
    
    #Get positions of spaces from 'text'. The beggining of 'text'
    #is initialized with -1
    spacestarts = [m.start() for m in re.finditer(' ', text)]
    spacestarts.append(-1)
    spacestarts.append(len(text))
    spacestarts.sort()
    
    #Startspaces affined by adding 1 to each position
    spacestarts_affine = [ss+1 for ss in spacestarts]
    spacestarts_affine.sort()
    
    #Get all the substrings that are between two spaces
    between_spaces = [(spacestarts[k] +1, spacestarts[k+1]) \
                      for k in range(0, len(spacestarts) -1)]
    
    #Find the spaces that are not valid
    between_spaces_notvalid = [loc for loc in between_spaces if \
                               text[loc[0]:loc[1]] not in word_list  ]
    print(between_spaces_notvalid)
    
    #Find the spaces that are not valid by using an imported corpus to check
    #valid words
    wordlist = set(brown.words())
    word_list = list(wordlist)
    
    #Remove special characters
    for sp in special_characters:
        word_list = [word.replace(sp, '') for word in word_list]
    word_list.remove('')

    between_spaces_notvalid = [loc for loc in between_spaces if \
                               text[loc[0]:loc[1]] not in word_list  ]
    print(between_spaces_notvalid)
    
    #check in word_list for words that could be combined to from
    #those invalid words
    partial_words = [loc for loc in locs if loc[0] in spacestarts_affine and \
                     loc[1] not in spacestarts]
    
    partial_words_end = [loc for loc in locs
                         if loc[0] not in spacestarts_affine and \
                         loc[1] in spacestarts]
    
    print(partial_words_end)



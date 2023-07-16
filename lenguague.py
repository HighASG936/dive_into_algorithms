import re

text = "The oneperfectly divine thing, the oneglimpse of God's paradisegiven on earth, is to fight a losingbattle - and notlose it."
word_list = ['The', 'one', 'perfectly', 'divine']

has_n = [word for word in word_list if 'n' in word]
print(has_n)

locs = list(set([ (m.start(), m.end()) for word in word_list for m in re.finditer(word, text) ]))

print(locs)



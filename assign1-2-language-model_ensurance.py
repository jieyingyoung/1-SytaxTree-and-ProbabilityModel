import re
import jieba
from collections import Counter

path = 'C:/Users/psyji/Dropbox/data/AI_Course/ensurance_industry_dialog.txt'
FILE = open(path, encoding='utf-8', mode = 'r').read()

# clean the data: Capital letters, ++$++ symples, - as white blank , ? question mark
FILE = FILE.lower() # to make the capital letters into lower case
FILE = FILE.replace('++$++', '') # to remove the symble
FILE = FILE.replace('?', '') # to remove the English question mark
FILE = FILE.replace('？', '') # to remove the Chinese question mark
FILE = FILE.replace('-', ' ') # to remove the Chinese question mark
FILE = re.sub(r"\d", "", FILE) # to remove all the digits
# FILE = re.sub(r"\w", "", FILE)  # if remove the white space, all the English words are together
print(FILE[:300])

# to cut the words
def cut(string):
    return list(jieba.cut(string.strip()))

tokens = cut(FILE) # a lot of blanks, would this be a problem?
print(tokens[:300])

word_count = Counter(tokens)
two_gram_words = [ tokens[i] + tokens[i+1] for i in range(len(tokens[:-1])) ]
bigram_words_counts = Counter(two_gram_words)

def gram_count(any_word, word_count):
    if any_word in word_count:
        return word_count[any_word]
    else:
        return word_count.most_common()[-1][-1]

def bigram_prob_model(sentence):
    tokens = cut(sentence)
    probability = 1
    for i in range(len(tokens)-1):
        word = tokens[i]
        next_word = tokens[i+1]
        prob = gram_count(word + next_word, bigram_words_counts) / gram_count(next_word, word_count)
        probability *= prob
    return probability

print(bigram_prob_model('我想买个保险'))
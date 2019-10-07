import re
import jieba
from collections import Counter

path = 'C:/Users/psyji/Dropbox/data/AI_Course/douban_movie_comments.txt'
FILE = open(path, encoding='utf-8', mode = 'r').read()

# clean the data: digit,English, url, .
def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)

FILE = remove_urls(FILE) # to remove the url
FILE = re.sub(r"\d|\W", "", FILE) # to remove all the digits and any non-word character, and remove the first line
print(FILE[:300])

# to cut the words
def cut(string):
    return list(jieba.cut(string.strip()))

tokens = cut(FILE)
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

print(bigram_prob_model('我很喜欢这个电影'))
## language model
## input: sentence(w1...wn)
## output: probability(0-1)

## 2-grams
## $$ Pr(sentence) = Pr(w_1 \cdot w_2 \cdots w_n) \prod \frac{count(w_i,w_{i+1})}{count(w_{i+1})} $$

import random
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

path = 'C:/Users/psyji/Dropbox/data/AI_Course/article_9k.txt'
FILE = open(path, encoding='utf-8', mode = 'r').read() # 'gbk' codec can't decode byte 0xaa in position 4: illegal multibyte sequence, if not specify the encoding method
max_length = 1000000
sub_file = FILE[:max_length]
print(len(FILE))
print(FILE[:500])

def cut(string):
    return list(jieba.cut(string))

tokens = cut(sub_file)
print(len(tokens))

word_count = Counter(tokens)
# print(word_count['我']

words_with_fre = [f for w,f in word_count.most_common(1000)]
# print(word_count.most_common(100))

def show_plt(data):
    plt.plot(data)
    plt.show()

# show_plt(words_with_fre)
# show_plt(np.log(words_with_fre))
# show_plt(np.log(np.log(words_with_fre)))

two_gram_words = [
    tokens[i] + tokens[i+1] for i in range(len(tokens[:-1]))
]

bigram_words_counts = Counter(two_gram_words)
# print(bigram_words_counts['我认为'])

def one_gram_count(word):
    if word in word_count: return word_count[word]
    else:
        return word_count.most_common()[-1][-1]
        # if it doesn't in the text, then it has the count of the last word in 'most common, which is the least common one, probabaly 1

def two_gram_count(bigram):
    if bigram in bigram_words_counts:
        return bigram_words_counts[bigram]
    else:
        return bigram_words_counts.most_common()[-1][-1]
    # one gram and two grams are the same , so combine them into one function

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

print(bigram_prob_model('前天晚上吃早饭的时候'))

def generate_by_random(text, length):
    return ''.join(random.sample(text,length)) # generate a sentence with 20 characters randomly

# print(generate_by_random(FILE,20)) # try to generate a sentence with 20 characters randomly

# print(list(jieba.cut(FILE[:100]))) # try jieba cut

# 2-gram => 3-gram

tregram_words = [
    tokens[i] + tokens[i+1] + tokens[i + 2 ]for i in range(len(tokens[:-2]))
]

tregram_words_counts = Counter(tregram_words)

def tregram_prob_model(sentence):
    tokens = cut(sentence)
    probability = 1
    for i in range(len(tokens)-2):
        word = tokens[i]
        next_word = tokens[i+1]
        next_next_word = tokens[i+2]
        prob = gram_count(word + next_word + next_next_word, tregram_words_counts) / gram_count(next_word + next_next_word, bigram_words_counts)
        probability *= prob
    return probability

print(tregram_prob_model('前天晚上吃早饭的时候'))
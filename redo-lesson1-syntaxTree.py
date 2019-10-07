# This is the re-coding of the lecture made by Minquan Gao, 28Sep 2019
import random

hello_rules = '''
say_hello = name hello tail
names = name names | name
name = Mike | Jessie | 老梁 | 死鬼 | 恶魔
hello = 你好 | 您来了 | 您请进
tail = 呀 | ! | 呢 
'''
 # three quoats can make each line prints as a single line and someone said you can suprisingly add 'mark down ' in the string but I didn't make it

simple_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => Adj | Adj Adj*
verb_phrase => verb noun_phrase
Article =>  一个 | 这个
noun =>   女人 |  篮球 | 桌子 | 小猫
verb => 看着   |  坐在 |  听着 | 看见
Adj =>   蓝色的 |  好看的 | 小小的
"""

simple_programming = '''
if_stmt => if ( cond ) { stmt }
cond => var op var
op => | == | < | >= | <= 
stmt => assign | if_stmt
assign => var = var
var =>  char var | char
char => a | b |  c | d | 0 | 1 | 2 | 3
'''

def name():
    return random.choice('Mike | Jessie | 老梁 | 老李 '.split('|'))

def hello():
    return random.choice('你好 | 您来了 | 您请进'.split('|'))

def tail():
    return random.choice('呀 | ! '.split('|'))

def say_hello():
    return name() + '' + hello() + '' + tail()

# print(name () + hello() + tail())

def generate(gramma_rule, target): # gramma_rule is a dictionary, target is the key
    if target in gramma_rule: # because target may not in the gramma_rule
        candidates = gramma_rule[target]  # take the contents of the dictionary gramma_rule , which key is 'target'
        # candidates = [c.strip() for c in candidates] # to remove the whitespace
        candidate = random.choice(candidates) #randomly take one of the candidates
        again = [generate(gramma_rule,target = c.strip()) for c in candidate.split()] # for the case of 'name names', then repeat itself
        return ''.join(again) # to remove the whitespace in candidate
    else:
        return target

def get_generation_by_gram(gramma_str, target, equal_split = '=', or_split = '|'):
    rules = dict()

    for line in gramma_str.split('\n'):
        if not line: continue # skip the empty lines
        key, contents = line.split(equal_split)
        content = contents.split(or_split)
        #print(key,'\n',content)
        rules[key.strip()] = content
        # strip(): returns a new string after removing any leading and trailing whitespaces including tabs (\t).
        # rstrip(): returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
        # lstrip(): returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.

    generated = generate(rules,target = target)
    return generated


print(get_generation_by_gram(hello_rules,'say_hello'))

print(get_generation_by_gram(simple_grammar, target = 'sentence', equal_split= '=>'))

# locals()  , see how many local variables are stored in the jupyter notebook

print(get_generation_by_gram(simple_programming, target = 'if_stmt', equal_split= '=>'))

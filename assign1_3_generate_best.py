import random
from assign1_2_language_model_movie import bigram_prob_model
from assign1_1_generate_sentence import generate_n, poem

def generate_best(rules,target,number_sentence):
    generate_sentences = generate_n(rules, target, number_sentence)
    sentence_with_prob = [(each,bigram_prob_model(each)) for each in generate_sentences]
    # print(sentence_with_prob)
    sorted_sentence = sorted(sentence_with_prob, key=lambda x: x[1], reverse=True)
    return sorted_sentence[0]

print(generate_best(poem, 'yongE', 4))
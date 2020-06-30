#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:21:48 2020

@author: naijain
"""
import nltk 
from nltk.corpus import wordnet

# Word Negation Tracking

sentence = "I was not happy with my team's performance."

# not happy = not_happy or unhappy

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ""

for word in words:
    antonyms = []
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) > 0:
            word = antonyms[0]
        else:
            word = temp_word + word
        temp_word = ""
    if word != "not":
        new_words.append(word)
        
sentence = ' '.join(new_words)
print(sentence)
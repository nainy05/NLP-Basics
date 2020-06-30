#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:21:48 2020

@author: naijain
"""
import nltk 

# Word Negation Tracking

sentence = "I was not happy with my team's performance."

# not happy = not_happy or unhappy

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ""

for word in words:
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        word = temp_word  + word
        temp_word = ""
    if word != "not":
        new_words.append(word)
        
sentence = ' '.join(new_words)
print(sentence)
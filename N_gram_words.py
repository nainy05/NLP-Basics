#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:11:45 2020

@author: naijain
"""


import nltk
import random

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

n = 3

ngrams = {}

# Create n-gram mappings
words = nltk.word_tokenize(text)
for i in range(len(words) - n):
    gram = ' '.join(words[i:i+n])
    next = ""
    if i+n < len(words):
        next = words[i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(next)

# Testing our n-gram model
currentGram = ' '.join(words[0:n])

result = currentGram

for i in range(30):
    if currentGram  not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += ' ' + nextItem
    currentGram = ' '.join(nltk.word_tokenize(currentGram)[1:]) + ' ' +nextItem

print(result)
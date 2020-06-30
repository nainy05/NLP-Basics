#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:52:05 2020

@author: naijain
"""


import nltk
import numpy as np


paragraph = """Thank you all so very much. Thank you to the Academy. 
               Thank you to all of you in this room. I have to congratulate 
               the other incredible nominees this year. The Revenant was 
               the product of the tireless efforts of an unbelievable cast
               and crew. First off, to my brother in this endeavor, Mr. Tom 
               Hardy. Tom, your talent on screen can only be surpassed by 
               your friendship off screen … thank you for creating a t
               ranscendent cinematic experience. Thank you to everybody at 
               Fox and New Regency … my entire team. I have to thank 
               everyone from the very onset of my career … To my parents; 
               none of this would be possible without you. And to my 
               friends, I love you dearly; you know who you are. And lastly,
               I just want to say this: Making The Revenant was about
               man's relationship to the natural world. A world that we
               collectively felt in 2015 as the hottest year in recorded
               history. Our production needed to move to the southern
               tip of this planet just to be able to find snow. Climate
               change is real, it is happening right now. It is the most
               urgent threat facing our entire species, and we need to work
               collectively together and stop procrastinating. We need to
               support leaders around the world who do not speak for the 
               big polluters, but who speak for all of humanity, for the
               indigenous people of the world, for the billions and 
               billions of underprivileged people out there who would be
               most affected by this. For our children’s children, and 
               for those people out there whose voices have been drowned
               out by the politics of greed. I thank you all for this 
               amazing award tonight. Let us not take this planet for 
               granted. I do not take tonight for granted. Thank you so very much."""
               
sentences = nltk.sent_tokenize(paragraph)
words = nltk.word_tokenize(paragraph)
words = [word.lower() for word in words if word.isalnum()]

word_freq = {}

for word in words:
    if word in word_freq.keys():
        word_freq[word] = word_freq[word] + 1
    else:
        word_freq[word] = 1

most_freq_words = word_freq.keys()
most_freq_words = sorted(most_freq_words, key = lambda word : -word_freq[word])
most_freq_words = most_freq_words[:100]
for word in most_freq_words:
    print(word, word_freq[word])

X = []
for doc in sentences:
    vector = []
    for word in most_freq_words:
        if word in nltk.word_tokenize(doc):
            vector.append(1)
        else:
            vector.append(0)
    X.append(vector)
    
    
X = np.asarray(X)
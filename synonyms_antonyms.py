#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:56:48 2020

@author: naijain
"""


# Finding synonyms and antonyms

from nltk.corpus import wordnet 

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())

synonyms = set(synonyms)
antonyms = set(antonyms)
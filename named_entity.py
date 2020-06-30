#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:32:54 2020

@author: naijain
"""


import nltk

paragraph = "The Taj Mahal was built by Emperor Shah Jahan"

words = nltk.word_tokenize(paragraph)
tagged_words = nltk.pos_tag(words)

namedEnt = nltk.ne_chunk(tagged_words)
namedEnt.draw()
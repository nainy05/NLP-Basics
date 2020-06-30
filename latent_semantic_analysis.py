#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:12:10 2020

@author: naijain
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import nltk

# Sample Data
dataset = ["The amount of polution is increasing day by day",
           "The concert was just great",
           "I love to see Gordon Ramsay cook",
           "Google is introducing a new technology",
           "AI Robots are examples of great technology present today",
           "All of us were singing in the concert",
           "We have launch campaigns to stop pollution and global warming"]

# Pre process data
dataset = [line.lower() for line in dataset]

# converts dataset to tfidf and provides other features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

print(X[0])

lsa = TruncatedSVD(n_components = 4, n_iter = 100)
lsa.fit(X)

row1 = lsa.components_[0]

concept_words =  {}
terms = vectorizer.get_feature_names()

for i, comp in enumerate((lsa.components_)):
    component_terms = zip(terms,comp)
    sorted_terms = sorted(component_terms, key=lambda x : -x[1])[:10]
    print("\nConcept",i,":")
    for term in sorted_terms:
        print(term)
    concept_words["Concept ", str(i)] = sorted_terms

for key in concept_words.keys():
    sentence_scores = []
    for sentence in dataset:
        words = nltk.word_tokenize(sentence)
        score = 0
        for word in words:
            for word_with_score in concept_words[key]:
                if(word == word_with_score[0]):
                    score += word_with_score[1]
        sentence_scores.append(score)
    print("\n" , key , ":")
    print(sentence_scores)
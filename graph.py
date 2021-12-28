# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:08:34 2021

@author: TUBA
"""

import numpy as np
import math
from math import*
from sentence_transformers import SentenceTransformer
from decimal import Decimal

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def manhattan_distance(x,y): 
    return sum(abs(a-b) for a,b in zip(x,y))

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)
 
def minkowski_distance(x,y):
    p_value=3
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

def createGraph(sentences):
    # bert-base-nli-mean-tokens
    # roberta-base-nli-stsb-mean-tokens
    # distilbert-base-nli-stsb-mean-tokens
    # bert-base-nli-stsb-mean-tokens
    model = SentenceTransformer('roberta-base-nli-stsb-mean-tokens') #The sentence transform models mentioned above can be used.
    sentence_embeddings = model.encode(sentences)
    sentenceGraph =np.zeros((len(sentences), len(sentences)))
    temp = np.arange(len(sentences))
    for x in range(len(sentences)):
        newTemp= np.delete(temp, x)
        for y in newTemp:
            similarity= cosine(sentence_embeddings[x],sentence_embeddings[y]) # You can change the vector similarity measurement method used when creating graphs. Cosine, euclidean, manhattan and minkowski methods are defined.
            sentenceGraph[x][y]=similarity
    return sentenceGraph


def findHighestSimilarityRank(similarityMatrix, initialRank):
    newRank=[0] * len(similarityMatrix)
    temp=0
    for i in range(len(similarityMatrix)):
        for j in range(len(similarityMatrix)):
            temp=temp+similarityMatrix[i][j] # sum of total similarity of sentences
        newRank[i]=temp*initialRank[i]
        temp=0

    return newRank
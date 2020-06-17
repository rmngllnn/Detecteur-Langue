#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:19:26 2020

@authors: Romane GALLIENNE, Cindy PEREIRA, Nadège DEMANÉE
"""

import string as str
from nltk import ngrams
import pickle
import re
import math

"""
Questionnement : est-ce qu'on ferait pas une fonction nettoyage (comme en JAVA)
pour enlever tout ce qui nous gêne (ponctuation, signes API), et qu'on peut
modifier selon les petits trucs qu'on rencontre qui nous embêtent
"""


#Fonction qui enlève la ponctuation. Fonctionne
def punct_less(text):
    for punct in str.punctuation:
        text = text.replace(punct, "")
    return text


#Fonction qui enlève les nombres (utile ?). Fonctionne
def numb_less(texte):
    return re.sub("[0-9]+", "", texte)


#Génère une liste de ngramme
def separate(texte, n) :
    txt_ngrams = list(ngrams(texte, n))
    return txt_ngrams

#crée un dictionnaire
def createDico(texte) :
    list_ngrams = separate(texte, 2)
    dict = {} #on crée un dictionnaire vide
    for gram in list_ngrams :
        if gram not in dict:
            dict[gram] = 0 #la clé ne devrait-elle pas être initialisé à 1 ?!
        dict[gram] += 1
    return dict

#calcul des similarités par la distance euclidienne
def similariteDistanceEuclidienne(dicoCorpus, dicoTrain) :
    distance = 0
    for elmt in set(dicoCorpus.keys()).intersection(dicoTrain.keys()) :
        distance += (dicoCorpus[elmt]-dicoTrain[elmt])**2
    return math.sqrt(distance)

#calcul des similarités par similarité des cosinus
def similariteCosinus(dicoCorpus, dicoTrain) :
    prodScal, normCorpus, normTrain = 0, 0, 0
    for elmt in set(dicoCorpus.keys()).intersection(dicoTrain.keys()) :
        prodScal += dicoCorpus[elmt]*dicoTrain[elmt]
        normCorpus += dicoCorpus[elmt]**2
        normTrain += dicoTrain[elmt]**2
    norm = math.sqrt(normCorpus)*math.sqrt(normTrain)
    return prodScal / norm

# On ouvre un fichier
def readFile(fileName) :
    fic = open(fileName, "r")
    text = fic.read()
    fic.close()
    return text

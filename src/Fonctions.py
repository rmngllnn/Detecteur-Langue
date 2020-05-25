#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:19:26 2020

@authors: Romane GALLIENNE, Cindy PEREIRA, Nadège DEMANÉE
"""

import string as str
from nltk import ngrams
import numpy as np
import pickle
import bz2
import _pickle as cPickle
from math import sqrt

"""
Questionnement : est-ce qu'on ferait pas une fonction nettoyage (comme en JAVA)
pour enlever tout ce qui nous gêne (ponctuation, signes API), et qu'on peut
modifier selon les petits trucs qu'on rencontre qui nous embêtent
"""


#Fonction qui enlève la ponctuation. Fonctionne
def punct_less(texte):
    for punct in str.punctuation:
        texte = texte.replace(punct, "")
    return texte

#Fonction qui enlève les signes API
def api_less(texte):
    pass


#Fonction qui enlève les nombres (utile ?). Fonctionne
def numb_less(texte):
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for num in numbers :
        texte = texte.replace(num, "")
    return texte


#Génère une liste de bigramme (en tuple je crois)
def separate(texte, n) :
    txt_ngrams = list(ngrams(texte, n))
    return txt_ngrams

#bigrammes = ngrams("Republic of Afghanistan, is a landlocked country comm in South and Central Asia.")
#print(bigrammes)


def createDico(texte) :
    list_ngrams = separate(texte, 2)
    dict = {} #on crée un dictionnaire vide
    for gram in list_ngrams :
        if gram not in dict:
            dict[gram] = 0 #il crée la clé qui lui donne une valeur
        dict[gram] += 1
    return dict


def similariteCosinus(dicoCorpus, dicoTrain) :
    prodScal = 0
    for elmt in set(dicoCorpus.keys()).intersection(dicoTrain.keys()) :
        prodScal += dicoCorpus[elmt]*dicoCorpus[elmt]
        normCorpus += dicoCorpus[elmt]^2
        normTrain += dicoTrain[elmt]^2
    norm = math.sqrt(normCorpus)*math.sqrt(normTrain)
    return prodScal / norm

# On ouvre un fichier
def readFile(fileName) :
    fic = open(fileName, "r")
    text = fic.read()
    fic.close()
    return text

# Load any compressed pickle file
def decompress_pickle(fileName):
    data = bz2.BZ2File(fileName, 'rb')
    data = cPickle.load(data)
    return data

'''
# Récupération du dictionnaire de corpus test Francais :
fileName = 'variables/FrancaisDico.pbz2'
dicoAnglais = decompress_pickle(fileName)
#print(dicoAnglais)
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:19:26 2020

@authors: Romane GALLIENNE, Cindy PEREIRA, Nadège DEMANEE
"""

import string as str
import nltk
from nltk import bigrams

"""
Questionnement : est-ce qu'on ferait pas une fonction nettoyage (comme en JAVA)
pour enlever tout ce qui nous gêne (ponctuation, signes API), et qu'on peut
modifier selon les petits trucs qu'on rencontre qui nous embête
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
def ngrams(texte) :
    txt_bigrams = list(bigrams(texte))
    return txtBigrams


print(ngrams("Republic of Afghanistan, is a landlocked country in South and Central Asia."))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@authors: Romane GALLIENNE, Cindy PEREIRA
"""

from Fonctions import createDico
from Fonctions import readFile
import os
#from pathlib import Path
import pickle
from sys import argv

"""
Fichier permettant de vectoriser les corpus tests
NE PAS LANCER, LES VARIABLES SONT DEJA SAUVEGARDEES
"""

def recuperationTextesCorpus(langue) :
    path = os.getcwd()
    directory = os.path.abspath(os.path.join(path, os.pardir)) + '/Corpus/' + langue
    txt = ""
    for fileName in os.listdir(directory) :
        txt += readFile(directory + "/" + fileName)
    return txt

def recuperationDico(langue, n) :
    text = recuperationTextesCorpus(langue)
    dico = createDico(text, n)
    fileName = os.getcwd() + '/variables/' + langue + 'Dico' + str(n) + '.pkl'
    f = open(fileName, 'wb')
    pickle.dump(dico, f)
    f.close()


n = 0
if len(argv) > 1 :
    n = int(argv[1])
    
recuperationDico("anglais", n)
recuperationDico("allemand", n)
recuperationDico("espagnol", n)
recuperationDico("francais", n)
recuperationDico("portugais", n)

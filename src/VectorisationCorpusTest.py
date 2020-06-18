#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@authors: Romane GALLIENNE, Cindy PEREIRA
"""

from Fonctions import *
import os
from pathlib import Path
import numpy as np
import pickle
import bz2
import _pickle as cPickle


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

def recuperationDico(langue) :
    text = recuperationTextesCorpus(langue)
    dico = createDico(text)
    fileName = os.getcwd() + '/variables/' + langue + 'DicoTrigramme.pkl'
    f = open(fileName, 'wb')
    pickle.dump(dico, f)
    f.close()


recuperationDico("anglais")
recuperationDico("allemand")
recuperationDico("espagnol")
recuperationDico("francais")
recuperationDico("portugais")

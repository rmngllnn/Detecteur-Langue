#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@authors: Romane GALLIENNE, Cindy PEREIRA, Nadège DEMANÉE
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

def recuperationTextes(langue) :
    path = os.getcwd()
    directory = os.path.abspath(os.path.join(path, os.pardir)) + '/Corpus/' + langue
    txt = ""
    for fileName in os.listdir(directory) :
        txt += readFile(directory + "/" + fileName)
    return txt

def recuperationDico(langue) :
    text = recuperationTextes(langue)
    dico = createDico(text)
    f = open("variables/" + langue + "Dico" + ".pkl", 'wb')
    pickle.dump(dico, f)
    f.close()


recuperationDico("Anglais")
recuperationDico("Allemand")
recuperationDico("Espagnol")
recuperationDico("Francais")
recuperationDico("Portugais")

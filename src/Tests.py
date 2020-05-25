from Fonctions import *
import sys
import numpy as np
from numpy.linalg import norm

'''
A LANCER AVEC UN NOM DE FICHIER EN ARGUMENT
'''



def comp(text, language) :
    fileName = 'variables/' + language + 'Dico.pbz2'
    dicoCorp = decompress_pickle(fileName)
    data = np.load('variables/' + language + 'Vector.npy')
    vectorCorp = data['vector']
    vector, _ = vectorisation(txt, dicoCorp)
    similarite = similariteCosinus(dicoCorpus, dicoTrain)
    return similarite

def maxSim(liste) :
    indMax = 0
    for i in range (0, len(liste)) :
        if liste[i] > liste[indMax] :
            indMax = i
    return indMax

if len(sys.argv) > 1 :
    txt = readFile(sys.argv[1])
    simList = []
    simAll = comp(txt, "Allemand")
    simList.append(simAll)
    simAng = comp(txt, "Anglais")
    simList.append(simAng)
    simEs = comp(txt, "Espagnol")
    simList.append(simEs)
    simFr = comp(txt, "Francais")
    simList.append(simFr)
    simPt = comp(txt, "Portugais")
    simList.append(simPt)

    print("Allemand : ", simAll)
    print("Anglais : ", simAng)
    print("Espagnol : ", simEs)
    print("Francais : ", simFr)
    print("Portugais : ", simPt)

    ind = maxSim(simList)

    languages = ["Allemand", "Anglais", "Espagnol", "Francais", "Portugais"]
    print("Le texte semble être en ", languages[ind])

from Fonctions import numb_less
from Fonctions import createDico
from Fonctions import similariteCosinus
from Fonctions import similariteDistanceEuclidienne
from Fonctions import readFile

from sys import argv
import os
import pickle

'''
A LANCER AVEC UN N ET UN NOM DE FICHIER EN ARGUMENT
'''

def similarite(dicoTrain, language, n) :
    fileName = os.getcwd() + '/variables/' + language + 'Dico' + str(n) + '.pkl'
    data = open(fileName, 'rb')
    dicoCorpus = pickle.load(data)
    data.close()
    return similariteCosinus(dicoCorpus, dicoTrain), similariteDistanceEuclidienne(dicoCorpus, dicoTrain)

#fonction pour chercher la similarité la plus grande
def maxSim(liste) :
    indMax = 0
    for i in range (0, len(liste)) :
        if liste[i] > liste[indMax] :
            indMax = i
    return indMax


#Test car on doit chercher la distance euclidienne la plus petite
#Après qqs tests, ça ne change rien a priori
#à voir si ce que j'ai fait est correct aussi mais je crois pas
def minSim(liste) :
    indMin = 0
    for i in range (0, len(liste)) :
        if liste[i] < liste[indMin] :
            indMin = i
    return indMin


def calculLangue(liste1, liste2, langue, dicoTrain, n) :
    sim1, sim2 = similarite(dicoTrain, langue, n)
    liste1.append(sim1)
    liste2.append(sim2)
    print(langue, "cos ->", sim1, "DE ->", sim2)

langues = ["allemand", "anglais", "espagnol", "francais", "portugais"]

print()
if len(argv) > 2 :
    txt = ""
    n = int(argv[1])
    if os.path.isfile(argv[2]) :
        txt = readFile(argv[2])
    else :
        words = argv[2:]
        for word in words :
            txt += word + " "
    txt = numb_less(txt)
    dicoTrain = createDico(txt, n)
    liste1, liste2 = [], []

    for langue in langues :
        calculLangue(liste1, liste2, langue, dicoTrain, n)


    indCos = maxSim(liste1)
    indDE = minSim(liste2)

    print()
    print("D'après le cosinus, le texte semble être en", langues[indCos])
    print("D'après la distance euclidienne, le texte semble être en", langues[indDE])

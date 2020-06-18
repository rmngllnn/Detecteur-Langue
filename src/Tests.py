from Fonctions import *
import sys
import os

'''
A LANCER AVEC UN NOM DE FICHIER EN ARGUMENT
'''

def similarite(dicoTrain, language) :
    fileName = os.getcwd() + '/variables/' + language + 'DicoTrigramme.pkl'
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
    indMax = max(liste)
    for i in range (0, len(liste)) :
        if liste[i] < indMax :
            indMax = i
    return indMax


def calculLangue(liste1, liste2, langue, dicoTrain) :
    sim1, sim2 = similarite(dicoTrain, langue)
    liste1.append(sim1)
    liste2.append(sim2)
    print(langue + "cos ->", sim1, "DE ->", sim2)

langues = ["allemand", "anglais", "espagnol", "francais", "portugais"]

if len(sys.argv) > 1 :
    txt = readFile(sys.argv[1])
    txt = numb_less(txt)
    dicoTrain = createDico(txt)
    liste1, liste2 = [], []

    for langue in langues :
        calculLangue(liste1, liste2, langue, dicoTrain)


    indCos = maxSim(liste1)
    indDE = minSim(liste2)

    print()
    print("D'après le cosinus, le texte semble être en", langues[indCos])
    print("D'après la distance euclidienne, le texte semble être en", langues[indDE])

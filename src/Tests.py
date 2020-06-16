from Fonctions import *
import sys

'''
A LANCER AVEC UN NOM DE FICHIER EN ARGUMENT
'''

import matplotlib.pyplot as plt


def similarite(dicoTrain, language) :
    fileName = 'variables/' + language + 'Dico.pkl'
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
#Après qqs tests, ne changentrien a priori (à voir si ce que j'ai fait est correct aussi)
def minSim(liste) :
    indMax = max(liste)
    for i in range (0, len(liste)) :
        if liste[i] < indMax :
            indMax = i
    return indMax



if len(sys.argv) > 1 :
    txt = readFile(sys.argv[1])
    txt = numb_less(txt)
    dicoTrain = createDico(txt)

#création des listes de similarités pour étiqueter la langue du texte
    simListCos, simListDE = [], []
    simAllCos, simAllDE = similarite(dicoTrain, "Allemand")
    simListCos.append(simAllCos)
    simListDE.append(simAllDE)
    simAngCos, simAngDE = similarite(dicoTrain, "Anglais")
    simListCos.append(simAngCos)
    simListDE.append(simAngDE)
    simEsCos, simEsDE = similarite(dicoTrain, "Espagnol")
    simListCos.append(simEsCos)
    simListDE.append(simEsDE)
    simFrCos, simFrDE = similarite(dicoTrain, "Francais")
    simListCos.append(simFrCos)
    simListDE.append(simFrDE)
    simPtCos, simPtDE = similarite(dicoTrain, "Portugais")
    simListCos.append(simPtCos)
    simListDE.append(simPtDE)

    print("Allemand : cos ->", simAllCos, "DE ->", simAllDE)
    print("Anglais : cos ->", simAngCos, "DE ->", simAngDE)
    print("Espagnol : cos ->", simEsCos, "DE ->", simEsDE)
    print("Francais : cos ->", simFrCos, "DE ->", simFrDE)
    print("Portugais : cos ->", simPtCos, "DE ->", simPtDE)

    indCos = maxSim(simListCos)
    indDE = minSim(simListDE)

    langages = ["Allemand", "Anglais", "Espagnol", "Francais", "Portugais"]
    print()
    print("D'après le cosinus, le texte semble être en", langages[indCos])
    print("D'après la distance euclidienne, le texte semble être en", langages[indDE])

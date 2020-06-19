import os
from pathlib import Path
from Fonctions import recuperationTextes
from Fonctions import createDico
from Fonctions import numb_less

from Tests import calculLangue
from Tests import maxSim
from Tests import minSim

from sys import argv

#n = 0
if len(argv) > 1 :
    n = int(argv[1])

langues = ["allemand", "anglais", "espagnol", "francais", "portugais"]
textes = []

for langue in langues :
    textes.extend(recuperationTextes(langue))


# 0 <= i <= 8 : allemand
# 9 <= i <= 17 : Anglais
# 18 <= i <= 26 : Espagnol
# 27 <= i <= 35 : Francais
# 36 <= i <= 44 : portugais

languesTextes = ["allemand"]*9
languesTextes.extend(["anglais"]*9)
languesTextes.extend(["espagnol"]*9)
languesTextes.extend(["francais"]*9)
languesTextes.extend(["portugais"]*9)


testsCos, testsDE = [], []
tailleTextes = []
i = 0

for texte in textes :
    tailleTextes.append(len(texte))
    texte = numb_less(texte)
    dicoTrain = createDico(texte, n)
    liste1, liste2 = [], []

    for langue in langues :
        calculLangue(liste1, liste2, langue, dicoTrain, n)

    indCos = maxSim(liste1)
    indDE = minSim(liste2)

    #print("Cos :", langues[indCos], languesTextes[i])
    #print("DE :", langues[indDE], languesTextes[i])
    if langues[indCos] == languesTextes[i] :
        testsCos.append(True)
    elif langues[indCos] != languesTextes[i]:
        testsCos.append(False)

    if langues[indDE] == languesTextes[i] :
        testsDE.append(True)
    elif langues[indDE] != languesTextes[i] :
        testsDE.append(False)

    i+=1
    #print()

def evaluation(liste):
    bonRes = 0
    for res in liste :
        if res == True :
            bonRes += 1
    return bonRes

def pourcentageParTaille(tailleTextes, testsCos) :
    print(tailleTextes)
    taillesUniq = []
    nbTextesParTaille = []
    nbCorrects = []

    for i in range (0, len(tailleTextes)) :
        if tailleTextes[i] not in taillesUniq :
            taillesUniq.append(tailleTextes[i])
            nbTextesParTaille.append(1)
            if testsCos[i] :
                nbCorrects.append(1)
            else :
                nbCorrects.append(0)
        else :
            index = taillesUniq.index(tailleTextes[i])
            nbTextesParTaille[index] += 1
            if testsCos[i] :
                nbCorrects[index] += 1

    pourcentages = []
    for i in range (0, len(nbTextesParTaille)) :
        pourcentages.append(nbCorrects[i]*100/nbTextesParTaille[i])

    return taillesUniq, pourcentages

    '''
    # Utilisation dico :
    # tailleDuTexte : [nombreDeFichiersDeCetteTailleCorrectementIdentifiés, nombreDeFichiersDeCetteTaille]
    taillePourcentage = {}
    for i in range (0, len(tailleTextes)) :

        if tailleTextes[i] not in taillePourcentage :
            if testsCos[i] :
                taillePourcentage[tailleTextes[i]] = [1, 1]
            else :
                taillePourcentage[tailleTextes[i]] = [0, 1]
        else :
            taillePourcentage[tailleTextes[i]][1] += 1
            if testsCos[i] :
                taillePourcentage[tailleTextes[i]][0] += 1
    pourcentages = []
    for key in taillePourcentage.keys() :
        pourcentages.append(taillePourcentage[key][0]*100 / taillePourcentage[key][1])
    return taillePourcentage.keys(), pourcentages
'''

print("Cos :", evaluation(testsCos)*100/len(testsCos), "/", 100)
print("DE :", evaluation(testsDE)*100/len(testsDE), "/", 100)

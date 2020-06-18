import os
from pathlib import Path
from Fonctions import *
from Tests import *


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
i = 0

for texte in textes :
    texte = numb_less(texte)
    dicoTrain = createDico(texte)
    liste1, liste2 = [], []

    for langue in langues :
        calculLangue(liste1, liste2, langue, dicoTrain)

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

print("Cos :", evaluation(testsCos)*100/len(testsCos), "/", 100)
print("DE :", evaluation(testsDE)*100/len(testsDE), "/", 100)

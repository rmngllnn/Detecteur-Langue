import os
from pathlib import Path
from Fonctions import *
from Tests import *

def recuperationTextes(langue) :
    path = os.getcwd()
    directory = os.path.abspath(os.path.join(path, os.pardir)) + '/CorpusTest/' + langue
    txt = []
    for fileName in os.listdir(directory) :
        txt.append(readFile(directory + "/" + fileName))
    return txt


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
i = 0
testsCos = []
testsDE = []
for texte in textes :
    texte = numb_less(texte)
    dicoTrain = createDico(texte)

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

    indCos = maxSim(simListCos)
    indDE = maxSim(simListDE)

    print("Cos :", langues[indCos], languesTextes[i])
    print("DE :", langues[indDE], languesTextes[i])

    if langues[indCos] == languesTextes[i] :
        testsCos.append(True)
    elif langues[indCos] != languesTextes[i]:
        testsCos.append(False)

    if langues[indDE] == languesTextes[i] :
        testsDE.append(True)
    elif langues[indDE] != languesTextes[i] :
        testsDE.append(False)

    i+=1
    print()

bonRes = 0
for res in testsCos :
    if res == True :
        bonRes += 1
print("Cos :", bonRes, "/", len(testsCos))

bonRes = 0
for res in testsDE :
    if res == True :
        bonRes +=1
print("DE :", bonRes, "/", len(testsDE))

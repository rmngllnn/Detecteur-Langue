#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:25:37 2020

@author: Romane GALLIENNE, Cindy PEREIRA
"""

'''
Dans le code, les graphiques sont codés par ordre alphabétique et non par
ordre d'affichage dans le terminal
'''


import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from Evaluation import *



#Pour comparer cosinus/distance euclidienne finale (pour l'évaluation)

fig = plt.figure()

x = ["Cosinus", "Distance\nEuclidienne"]
y = [evaluation(testsCos)*100/len(testsCos), evaluation(testsDE)*100/len(testsDE)]
width = 0.5


plt.bar(x, y, width, color='lightblue') #couleur cf. fichier CouleurMatplotlib.png
plt.title('Évaluation de performance entre\nla similarité de cosinus et la distance euclidienne')
plt.ylabel('Taux de réussite')
plt.ylim(0,100)
for x1,y1 in zip(x,y) :
    plt.annotate(y1,
                (x1,y1),
                textcoords="offset points",
                xytext=(0,-20),
                ha='center')
plt.show()

# Pour comparer la performance en fonction de la taille du texte

tailles, pourcentages = pourcentageParTaille(tailleTextes, testsCos)
plt.plot(tailles, pourcentages, 'o')
plt.ylim(0,110)
for x2,y2 in zip(tailles, pourcentages) :
    plt.annotate(y2,
                 (x2,y2),
                 textcoords="offset points",
                 xytext=(0,10), 
                 ha='center')

plt.title('Pourcentage de réussite en fonction\ndu nombre de caractères du texte')
plt.xlabel('Taille du texte en nombre de caractères')
plt.ylabel('Taux de réussite')
plt.show()

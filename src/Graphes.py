#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:25:37 2020

@author: romane
"""

'''
Dans le code, les graphiques sont codés par ordre alphabétique et non par
ordre d'affichage dans le terminal
'''

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


'''
#Pour comparer cosinus/distance euclidienne finale

fig = plt.figure()

x = ["Cosinus", "Distance\nEuclidienne"]
height = [1, 0.5]
width = 0.5

plt.bar(x, height, width, color='b' )
plt.title('Valeur du cosinus et de la distance euclidienne\n pour un texte')
plt.show()
'''




#Pour comparer cosinus/distance euclidienne pour chaque langue

names = ['Cosinus', 'Distance\neuclidienne']
values = [1, 0.5]

fig2 = plt.figure(constrained_layout=True)
spec2 = gridspec.GridSpec(ncols=3, nrows=3, figure=fig2)

allemand = fig2.add_subplot(spec2[2, 0])
plt.bar(names, values)
plt.title('Allemand')


anglais = fig2.add_subplot(spec2[0, 1])
plt.bar(names, values)
plt.title('Anglais')


espagnol = fig2.add_subplot(spec2[1, 0])
plt.bar(names, values)
plt.title('espagnol')


francais = fig2.add_subplot(spec2[0, 0])
plt.bar(names, values)
plt.title('français')


portugais = fig2.add_subplot(spec2[1, 1])
plt.bar(names, values)
plt.title('Portugais')


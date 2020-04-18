# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:37:21 2020

@author: Nicolas Rouvet
"""

import numpy as np
from pylab import plot

#création des différentes fonction aléatoire nécessaire

#
f=4

def Arrivee():
    arrivee = np.random.poisson(0.5)
    return arrivee

def ChoixEtage(f):
    choixEtage = round(np.random.uniform(1,f))
    return choixEtage

def tempsTravail():
    tempsTravail = np.random.exponential(60)
    return tempsTravail


def deroulementJournee(max):
    t = max*60 #convertir les heures en minutes
    personne =[0]*t
    i=0
    while(i<t):
        personne[i] = Arrivee()
        i+=1
    x = range(t)
    y = personne
    plot(x, y)
    return personne



print(deroulementJournee(5))

        






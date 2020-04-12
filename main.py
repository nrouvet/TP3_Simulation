# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:37:21 2020

@author: Nicolas Rouvet
"""

import numpy as np


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
    tempTravail = np.random.exponential(60)
    return tempsTravail







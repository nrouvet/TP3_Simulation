# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:37:21 2020

@author: Nicolas Rouvet
"""

import numpy as np
from pylab import plot


class Ascenseur:
    def _init_(self,etageT,etageD):
        self.t = 0
        self.d = []
        
    
        
    
#création des différentes fonction aléatoire nécessaire

#

personnes = []

class Personne:
    def __init__(self, etage, depart):
        self.etage = etage
        self.depart = depart        
        
f=4

def Arrivee():
    arrivee = np.random.poisson(0.5)
    return arrivee

def ChoixEtage(f):
    choixEtage = round(np.random.uniform(1,f))
    return choixEtage

def tempsTravail():
    tempsTravail = round(np.random.exponential(60))
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

def main():
    c = 0
    while(c<300):
        nb = Arrivee()
        i = 0
        while(i < nb):
            etage = ChoixEtage(f)
            temps = tempsTravail()
            pers = Personne(etage, temps)
            personnes.append(pers)
            i+=1
            
            
        c+=1
    
main()

        






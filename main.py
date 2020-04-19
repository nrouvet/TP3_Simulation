# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:37:21 2020

@author: Nicolas Rouvet
"""

import numpy as np
from pylab import plot


class Ascenseur:
    def __init__(self):
        self.current = 0
        self.etages = []
        self.disponibilite = True
        self.temps = 0 
        self.direction = "haut"
        self.capacite = []
        
    def order(self):
        tmp = []
        for e in self.etages:
            if(self.direction == "haut"):
                if(e < self.current):
                    tmp.append(e)
                    self.etages.remove(e)
            else:
                if(e > self.current):
                    tmp.append(e)
                    self.etages.remove(e) 
        if(self.direction=="haut"):
            tmp = tmp.sort(reverse = True)
        else:
            tmp = tmp.sort()
        for t in tmp:
            self.etages.append(t)                         
        
    def linearScan(self):
        if(self.direction == "haut"):
            self.etages = self.etages.sort()
        else:
            self.etages = self.etages.sort(reverse=True)
        self.order()   

    def deplacement(self, t):
        t -= 10
        if(t == self.temps):
            if(self.direction=="haut"):
                self.current += 1
            else:
                self.current -=1
            return True
        return False
    
    def sortieAcenseur(temps, self):
        for c in self.capacite:
            if (c.etage == self.current):
                c.attente = temps - c.arrivee
                tempsAttente.append(c.attente)
                self.capacite.remove(c)
        
    
#création des différentes fonction aléatoire nécessaire

#
tempsAttente = []
personnes = []

class Personne:
    def __init__(self, etage, depart, arrivee):
        self.etage = etage
        self.depart = depart
        self.arrivee = arrivee
        self.attente = 0        
        
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
    sec = 0  #Compteur secondes
    minute = 0  #Compteur minutes
    ascenseur = Ascenseur()
    while(sec<18000):  #18000s = 5h
        if(sec%60==0):
            nb = Arrivee()
            i = 0
            while(i < nb):
                etage = ChoixEtage(f)
                temps = tempsTravail() + minute
                pers = Personne(etage, temps, sec)
                personnes.append(pers)
                i+=1
                   
            for p in personnes:
                if(p.depart == minute):
                    etage = p.etage
                    if(etage not in ascenseur.etages):
                        ascenseur.etages.append(p.etage)
                    personnes.remove(p)
                    p.arrivee = sec
            minute+=1 
        
        sec+=1
    
main()

        






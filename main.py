# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:37:21 2020

@author: Nicolas Rouvet
"""

import numpy as np
from pylab import plot


class Ascenseur:
    def __init__(self):
        self.current = 0      #étage où se trouve l'ascenseur
        self.etages = []      #étages demandés
        self.disponibilite = True
        self.temps = 0          #calculer le temps de déplacement de l'ascenseur
        self.direction = "haut"
        self.capacite = []    #personnes dans l'ascenseur
        
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
            self.temps += 10   
            self.disponibilite = True
            return True
        self.disponibilite = False
        return False
    
    def sortieAcenseur(self, temps):
        for c in self.capacite:
            if (c.etage == self.current):
                c.attente = temps - c.arrivee * 60  #temps d'attente en seconde
                tempsAttente.append(c.attente)
                self.capacite.remove(c)
        
    
#création des différentes fonction aléatoire nécessaire

#
tempsAttente = []
personnes = []

class Personne:
    def __init__(self, etage, depart, arrivee):
        self.etage = etage   #étage demandé
        self.depart = depart    #temps où la personne part de l'immeuble
        self.arrivee = arrivee    #temps d'arrivée de la personne
        self.attente = 0        #utilisé pour calculé le temps d'attente de la personne
        
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
        
        ascenseur.deplacement(sec)
        if(ascenseur.disponibilite == True):
            ascenseur.sortieAcenseur(sec)
        
        sec+=1
    
main()

        






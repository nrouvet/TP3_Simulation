# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:37:21 2020

@author: Nicolas Rouvet
"""

import numpy as np
from pylab import plot
import matplotlib.pyplot as plt

class Ascenseur:
    def __init__(self):
        self.current = 0      #étage où se trouve l'ascenseur
        self.etages = []      #étages demandés
        self.disponibilite = True
        self.temps = 0          #calculer le temps de déplacement de l'ascenseur
        self.direction = "haut"
        self.capacite = []    #personnes dans l'ascenseur
        
    def arriveePersonne(self, personne):
        if(0 not in self.etages and self.current != 0):
            self.etages.append(0)
            
    def entreePersonne(self, personne):
        eta = personne.etage
        if(eta not in self.etages):
            self.etages.append(eta)
        self.capacite.append(personne)
        
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
           tmp.sort(reverse = True)
        else:
            tmp.sort()
        for t in tmp:
            self.etages.append(t)        
 
        
    def linearScan(self):
        if(self.direction == "haut"):
            self.etages.sort()
        else:
            self.etages.sort(reverse=True)
        self.order()   

    def changeDirection(self):
        if(len(self.etages) > 0):
            if(self.etages[0] < self.current):
                self.direction = "bas"
            if(self.etages[0] > self.current):
                self.direction = "haut"
            if(self.current == 0 ):
                self.direction = "haut"
            if(self.current == f):
                self.direction = "bas"
            

    def deplacement(self, t):
        if(len(self.etages)==0):
            self.temps = t
            return
        t -= 10
        if(t == self.temps):
            if(self.direction=="haut"):
                self.current += 1
            else:
                self.current -=1
            self.temps += 10   
            self.disponibilite = True
            if(self.current in self.etages):
                self.etages.remove(self.current)
            return
        self.disponibilite = False
        return
    
    def sortieAcenseur(self, temps):
        for c in self.capacite:
            if (c.etage == self.current):
                c.attente = temps - c.arrivee  #temps d'attente en seconde
                tempsAttente.append(c.attente)
                self.capacite.remove(c)
                if(self.current != 0):
                    personnes.append(c)
                    i = personnes.index(c)
                    personnes[i].etageAppel = personnes[i].etage
                    personnes[i].etage = 0
        
    
    
#création des différentes fonction aléatoire nécessaire

#
tempsAttente = []
personnes = []

class Personne:
    def __init__(self, etage, depart, arrivee):
        self.etage = etage   #étage demandé
        self.depart = depart    #temps où la personne part de l'immeuble (en minute)
        self.arrivee = arrivee    #temps d'arrivée de la personne  (en seconde)
        self.attente = 0        #utilisé pour calculé le temps d'attente de la personne (en seconde)
        self.etageAppel = 0
        
f=4
individu=[]
tempsJournee = 18000

def Arrivee():
    arrivee = np.random.poisson(0.5)
    return arrivee

def ChoixEtage(f):
    choixEtage = round(np.random.uniform(1,f))
    return choixEtage

def tempsTravail():
    tempsTravail = round(np.random.exponential(60))
    return tempsTravail


def deroulementJournee(time):
    
    x = range(time)
    y = individu
    plot(x, y)
    plt.figure()
    plt.bar(x,y,width = 0.4,color="r")
    plt.show()


def main():
    sec = 0  #Compteur secondes
    minute = 0  #Compteur minutes
    a = Ascenseur()
    tmp = []
    while(sec<tempsJournee):  #18000s = 5h
        if(sec%60==0):
            nb = Arrivee()
            i = 0
            individu.append(nb)
            while(i < nb):
                etage = ChoixEtage(f)
                temps = tempsTravail() + minute
                pers = Personne(etage, temps, sec)
                tmp.append(pers)
                a.arriveePersonne(pers)
                i+=1
                   
            for p in personnes:
                if(p.depart == minute):
                    etage = p.etageAppel
                    if(etage not in a.etages):
                        a.etages.append(p.etage)
                    tmp.append(p)
                    personnes.remove(p)
                    p.arrivee = sec
            minute+=1 
        
        a.deplacement(sec)
        #.linearScan()
        a.changeDirection()
        #print(a.etages, a.direction, a.current)
        
        
        if(a.disponibilite == True):
            a.sortieAcenseur(sec)
            for t in tmp:
                if(t.etageAppel == a.current):
                    a.entreePersonne(t)
        
        sec+=1
    
 

    
    

main()

deroulementJournee(int(tempsJournee/60))
moyenne= np.mean(tempsAttente)
mediane= np.median(tempsAttente)
print(moyenne,"sec" , mediane)





        






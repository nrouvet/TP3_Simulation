# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:37:21 2020

@author: Nicolas Rouvet
"""

import numpy as np
from pylab import plot
import matplotlib.pyplot as plt

class Ascenseur:
    def __init__(self, politique):
        self.politiqueDeplacement = politique
        self.current = 0      #étage où se trouve l'ascenseur
        self.etages = []      #étages demandés
        self.disponibilite = True
        self.temps = 0          #calculer le temps de déplacement de l'ascenseur
        self.direction = "haut"
        self.capacite = []    #personnes dans l'ascenseur
        
    def arriveePersonne(self, personne):
        if(milieu in self.etages and self.politiqueDeplacement == "milieu" and len(self.capacite) == 0 and self.current != 0):
            self.etages.remove(milieu)
        if(personne.etageAppel not in self.etages and self.current != 0):
            self.etages.append(personne.etageAppel)
            
    def entreePersonne(self, personne, temps):
        eta = personne.etage
        if(eta not in self.etages):
            self.etages.append(eta)
        self.capacite.append(personne)
        personne.attente = temps - personne.arrivee
        tempsAttente2.append(personne.attente)
        
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
            if(self.current in self.etages):
                self.etages.remove(self.current)    
                self.disponibilite = True
            return
        self.disponibilite = False
        return
    
    def sortieAcenseur(self, temps):
        for c in self.capacite:
            if (c.etage == self.current):
                self.capacite.remove(c)
                c.attente = temps - c.arrivee  #temps d'attente en seconde
                tempsAttente.append(c.attente)
                if(self.current != 0):
                    c.etageAppel = c.etage
                    c.etage = 0
                    personnes.append(c)
        if(self.politiqueDeplacement == "milieu" and len(self.capacite) == 0 and self.current != milieu):
            self.etages.append(milieu)
                    
        
    
    
#création des différentes fonction aléatoire nécessaire

#
tempsAttente = [] #temps d'attente de l'appel de l'ascenseur à la descente de l'ascenseur
tempsAttente2 = [] #temps d'attente de l'appel de l'ascenseur à la montée dans l'ascenseur
personnes = []

class Personne:
    def __init__(self, etage, depart, arrivee):
        self.etage = etage   #étage demandé
        self.depart = depart    #temps où la personne part de l'immeuble (en minute)
        self.arrivee = arrivee    #temps d'arrivée de la personne  (en seconde)
        self.attente = 0        #utilisé pour calculé le temps d'attente de la personne (en seconde)
        self.etageAppel = 0
        
f=4
milieu = int(f/2)
individu=[]
tempsJournee = 18000  #18000 sec = 5h

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


def main(politiqueMarche = "rester"):
    sec = 0  #Compteur secondes
    minute = 0  #Compteur minutes
    a1 = Ascenseur(politiqueMarche)
    a2 = Ascenseur(politiqueMarche)
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
                i+=1
                   
            for p in personnes:
                if(p.depart == minute):
                    etage = p.etageAppel
                    tmp.append(p)
                    personnes.remove(p)
                    p.arrivee = sec
                    
            for t in tmp:
                if(a1.current == t.etageAppel and a1.disponibilite == True):
                    a1.arriveePersonne(t)
                elif(a2.current == t.etageAppel and a2.disponibilite == True):
                    a2.arriveePersonne(t)
                elif(len(a1.etages) < len(a2.etages)):
                    a1.arriveePersonne(t)
                else:
                    a2.arriveePersonne(t)
                
            minute+=1 
        
        
        a1.deplacement(sec)
        a2.deplacement(sec)
        #a1.linearScan()
        #a2.linearScan()
        a1.changeDirection()
        a2.changeDirection()
        
        
        if(a1.disponibilite == True):
            a1.sortieAcenseur(sec)
            for t in tmp:
                if(t.etageAppel == a1.current):
                    a1.entreePersonne(t, sec)
                    tmp.remove(t)
        if(a2.disponibilite == True):
            a2.sortieAcenseur(sec)
            for t in tmp:
                if(t.etageAppel == a2.current):
                    a2.entreePersonne(t, sec)
                    tmp.remove(t)
        
        #print(a1.etages, a1.direction, a1.current, len(a1.capacite))
        #print(a2.etages, a2.direction, a2.current, len(a2.capacite))
        #print("\n")
        
        sec+=1
    
 

    
    

main("milieu")

deroulementJournee(int(tempsJournee/60))
moyenne= np.mean(tempsAttente)
mediane= np.median(tempsAttente)
moyenne2= np.mean(tempsAttente2)
mediane2= np.median(tempsAttente2)
print("Temps d'attente moyen : ", moyenne,"sec")
print("Temps d'attente médian : ", mediane, "sec")
print("Temps d'attente2 moyen : ", moyenne2,"sec")
print("Temps d'attente2 médian : ", mediane2, "sec")





        






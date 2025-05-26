# -*- coding: utf-8 -*-
"""
Created on Sat May 24 15:59:21 2025

@author: kylian
"""

# Lecture du fichier de dictionnaire et nettoyage des lignes
with open("frenchssaccent.dic","r") as fichier:
    lexique= [ligne.strip() for ligne in fichier.readlines()]

# Vérifie si un mot peut être formé avec les lettres d'un dictionnaire de tirage D
def possible(D,mot):
    for k in mot:
        if k not in D:
            return False
        if D[k]==0:
            return False
        D[k]-=1
    return True

# Cherche le mot le plus long possible dans la liste motpos, selon les lettres du tirage t
def pluslong(t,motpos):
    M=""
    D={}
    for i in t:
        if i in D:
            D[i]+=1
        else:
            D[i]=1
    s=0
    for i in motpos:
        if len(i)>s:
            S=len(i)
            if possible(D,i):
                M=i
                s=S
    return M

# Tirage de lettres
tirage = ['b', 'p', 'd', 'w', 's', 'y', 'w', 'i','o','g','a']
motspossibles = ['bis', 'bd']

# Autre exemple de tirage et de liste de mots possibles
tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
motspossibles = ['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser',"sac", 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']

# Affiche le mot le plus long formable avec le tirage
print(pluslong(tirage,motspossibles))

#%% Exercice 3

# Fonction de score Scrabble d'un mot
def score(mot,points):
    S=0
    for j in mot:
        S+=points[j]
    return S

# Calcule le mot ayant le score maximal dans une liste de mots
def max_score2(motpos):
    points={'a': 1,'e': 1, 'i': 1,'l': 1,'n': 1,'o': 1,'r': 1,'s': 1,'t': 1,'u': 1, "d":2,"g":2,"m":2,"b":3,"c":3,"P":3,"f":4,"h":4,"v":4,"j":4,"q":8,"k":10,"w":10,"x":10,"y":10,"z":10}
    M=""
    s=0
    for i in motpos:
        S=score(i,points)
        if S>s:
            M=i
            s=S
    return M,s

# Affiche le mot ayant le meilleur score dans la liste donnée
print(max_score2(['rte', 'ver', 'ce', 'etc', 'cet', 'ex', 'cr', 'et', 'ter', 'te', 'ct']))

#%% Exercice 4

# Recharge le lexique depuis le dictionnaire
with open("frenchssaccent.dic","r") as fichier:
    lexique= [ligne.strip() for ligne in fichier.readlines()]

# Vérifie si un mot peut être formé avec les lettres disponibles, y compris un joker "?"
def possible_score4(E,mot,points):
    S=0
    for k in mot:
        if k not in E:
            E[k]=0
        if ((E[k]==0) and (E["?"]==0)):
            return False
        if E[k]!=0:
            E[k]-=1
            S+=points[k]
        else: 
            if E['?']==1:
                E["?"]=0
    return S

# Trouve le mot du dictionnaire avec le score maximal possible, en prenant en compte un joker
def max_score(t):
    points={'a': 1,'e': 1, 'i': 1,'l': 1,'n': 1,'o': 1,'r': 1,'s': 1,'t': 1,'u': 1, "d":2,"g":2,"m":2,"b":3,"c":3,"P":3,"f":4,"h":4,"v":4,"j":4,"q":8,"k":10,"w":10,"x":10,"y":10,"z":10}
    M=""
    s=0
    D={"?":0}
    for i in t:
        if i in D:
            D[i]+=1
        else:
            D[i]=1
    for i in lexique:
        cD={j:D[j] for j in D}
        cD={j:D[j] for j in D}
        S=possible_score4(cD,i,points)
        if S>s:
            M=i
            s=S
    return M,s

# Exemple de tirage avec joker, retourne le mot le plus payant
print(max_score('zxcvrrt?'))
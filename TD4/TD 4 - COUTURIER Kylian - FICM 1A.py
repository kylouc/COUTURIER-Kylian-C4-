

# -*- coding: utf-8 -*-
"""
23 avril 2025 COUTURIER Kylian (FICM 1A)
Rendu à : khadidja-wissal.baki@univ.lorraine.fr
"""

# -------------------------------
# Q1-Q2 : Définir une fonction de hachage naïve et une classe Hashtable
# -------------------------------

def jh(s: str) -> int:
    """
    Fonction de hachage basée sur la méthode utilisée par Java (inspirée de Jenkins hash).
    Utilise un accumulateur avec un facteur de dispersion de 31.
    """
    h = 0
    for char in s:
        h = 31 * h + ord(char)
    return h if h < 2**31 else h - 2**32  # Gère les débordements éventuels

class Hashtable:
    @staticmethod
    def __naive_fct__(key):
        """
        Fonction de hachage naïve : somme des codes ASCII des caractères de la clé.
        """
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val

    def __init__(self, n, h):
        """
        Constructeur de la table de hachage.
        n : taille initiale de la table
        h : fonction de hachage (optionnelle)
        """
        self.size = n
        self.table = [[] for i in range(n)]  # Création d'une liste de listes (pour gérer les collisions)
        self.nbritem = 0  # Compteur d'éléments insérés
        self.function = h if h is not None else self.__naive_fct__  # Fonction de hachage par défaut

    def put(self, key, value):
        """
        Insère une paire (key, value) dans la table.
        Si la clé existe, met à jour la valeur.
        """
        a = self.function(key) % self.size  # Calcul de l'index par hachage
        for i in self.table[a]:
            if i[0] == key:
                i[1] = value  # Mise à jour si la clé existe déjà
                a = -1  # Empêche l'ajout en double
        if a != -1:
            self.table[a].append((key, value))  # Ajout si la clé est nouvelle

    def get(self, key):
        """
        Recherche la valeur associée à une clé.
        Renvoie None si la clé n'existe pas.
        """
        a = self.function(key) % self.size
        for i in self.table[a]:
            if i[0] == key:
                return i[1]
        return None

    def repartition(self):
        """
        Affiche un histogramme de la répartition des éléments dans les buckets.
        Permet de visualiser les collisions.
        """
        import matplotlib.pyplot as plt
        N = self.size
        x = range(N)
        y = [len(self.table[i]) for i in range(N)]
        width = 1 / 1.2
        plt.bar(x, y, width, color="blue")
        plt.show()

# -------------------------------
# Q3 : Test simple
# -------------------------------

ht = Hashtable(10, None)  # Création avec fonction de hachage par défaut
ht.put("aaa", 12)  # Insertion
print(ht.get("aaa"))  # Affiche 12
print(ht.get("abc"))  # Affiche None (clé absente)

# -------------------------------
# Q4-Q5 : Chargement d'un dictionnaire de mots
# -------------------------------

with open("frenchssaccent.dic", "r") as fichier:
    lexique = [ligne.strip() for ligne in fichier.readlines()]

# Test avec 320 buckets
lex = Hashtable(320, None)
for i in lexique:
    lex.put(i, len(i))
lex.repartition()  # Visualisation de la répartition

# Test avec 10 000 buckets
lex = Hashtable(10000, None)
for i in lexique:
    lex.put(i, len(i))
lex.repartition()

# Test avec une meilleure fonction de hachage
lex = Hashtable(320, jh)
for i in lexique:
    lex.put(i, len(i))
lex.repartition()

#%%
# -------------------------------
# Q6-Q7 : Redimensionnement automatique + mesure de performance
# -------------------------------

import time
tic = time.time()

# Redéfinir les classes pour inclure resize()

def jh(s: str) -> int:
    h = 0
    for char in s:
        h = 31 * h + ord(char)
    return h if h < 2**31 else h - 2**32

class Hashtable:
    @staticmethod
    def __naive_fct__(key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val

    def __init__(self, n, h):
        self.size = n
        self.table = [[] for i in range(n)]
        self.nbritem = 0
        self.function = h if h is not None else self.__naive_fct__

    def put(self, key, value):
        a = self.function(key) % self.size
        for i in self.table[a]:
            if i[0] == key:
                i[1] = value
                a = -1
        if a != -1:
            self.table[a].append((key, value))
            self.nbritem += 1
        # Redimensionnement si la densité dépasse 1.2
        if self.nbritem / self.size > 1.2:
            self.resize()

    def get(self, key):
        a = self.function(key) % self.size
        for i in self.table[a]:
            if i[0] == key:
                return i[1]
        return None

    def repartition(self):
        import matplotlib.pyplot as plt
        N = self.size
        x = range(N)
        y = [len(self.table[i]) for i in range(N)]
        width = 1 / 1.2
        plt.bar(x, y, width, color="blue")
        plt.show()

    def resize(self):
        """
        Double la taille de la table, puis réinsère tous les éléments existants.
        """
        old_items = []
        for bucket in self.table:
            old_items.extend(bucket)
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.nbritem = 0
        for key, value in old_items:
            self.put(key, value)

with open("frenchssaccent.dic", "r") as fichier:
    lexique = [ligne.strip() for ligne in fichier.readlines()]

lex = Hashtable(320, jh)
for i in lexique:
    lex.put(i, len(i))
lex.repartition()

# Temps d'insertion
tac = time.time()
print(tic - tac)

# Temps de lecture moyen
tic = time.time()
for i in lexique:
    lex.get(i)
tac = time.time()
print((tic - tac) / len(lexique))  # Temps moyen par accès

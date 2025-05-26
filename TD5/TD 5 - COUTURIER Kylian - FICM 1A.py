# -*- coding: utf-8 -*-
"""
Created on Mon May  5 23:04:48 2025

@author: kylian
"""

import tkinter as tk
from tkinter import Tk, Label, Frame
root = tk.Tk()  # Création de la fenêtre principale

def read_word(mot, h, w):
    # Crée un canvas de taille proportionnelle à la longueur du mot
    canvas = tk.Canvas(root, width=w*len(mot), height=h*len(mot))
    canvas.pack()

    x = 0  # Position de départ en x
    y = h * len(mot) / 2  # Position de départ en y (centré verticalement)

    for i in mot:
        if i == "H":  # Ligne horizontale vers la droite
            canvas.create_line(x, y, x+w, y, fill="blue", width=2)
            x += w
        if i == "U":  # Ligne en diagonale montante
            canvas.create_line(x, y, x+w, y-h, fill="blue", width=2)
            x += w
            y -= h
        if i == "D":  # Ligne en diagonale descendante
            canvas.create_line(x, y, x+w, y+h, fill="blue", width=2)
            x += w
            y += h

    root.mainloop()  

read_word("HUHHDUH", 30, 60)

#%%Q.2 à 6
import tkinter as tk
from tkinter import Tk, Label, Frame, Button
import numpy as np
root = tk.Tk()  # Nouvelle fenêtre

# Fonction principale de dessin d'entrelacement
def entrela(T, c):
    h = 40  # Hauteur d'un segment
    w = 30  # Largeur d'une colonne
    n = len(c)  # Nombre de "fils" 
    x0 = 10
    y0 = 10

    # Initialisation des positions de chaque fil
    L = [[x0, i * h + y0] for i in range(n)]

    # Création du canvas avec une taille dépendante du nombre d'étapes et de fils
    canvas = tk.Canvas(root, width= w*(len(T)+1)*2 , height=h *(n)+y0, bg="white")
    canvas.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    # Dessin des croisements
    for i in T:
        for k in range(len(L)):
            y = L[k][1]
            x = L[k][0]
            # Segment horizontal
            canvas.create_line(x, y, x + w, y, fill=c[k], width=2)
            x += w

            # Si le fil est impliqué dans un croisement
            if L[k][1] == i * h + y0:
                # Le fil descend
                canvas.create_line(x, y, x + w, y + h, fill=c[k], width=2)
                x += w
                y += h
            elif L[k][1] == (i + 1) * h + y0:
                # Le fil monte
                canvas.create_line(x, y, x + w, y - h, fill=c[k], width=2)
                x += w
                y -= h
            else:
                # Reste à la même hauteur
                canvas.create_line(x, y, x + w, y, fill=c[k], width=2)
                x += w

            # Mise à jour de la position du fil
            L[k] = [x, y]

    # Dernier segment horizontal pour chaque fil
    for k in range(len(L)):
        y = L[k][1]
        x = L[k][0]
        canvas.create_line(x, y, x + w, y, fill=c[k], width=2)
        x += w
        L[k] = [x, y]

    # Texte descriptif du croisement
    canvas.create_text(w* (len(T)+1),h*(n),  text=f"croisement:  {T}", fill="black", font=("Arial", int(2*np.log2(h)), "bold"))

# Fonction pour générer une permutation aléatoire des couleurs
def permutcol():
    import random as rd
    L0 = ["black", 'red', "green", "blue"]
    L = []

    # Mélange des couleurs
    for i in range(len(L0)):
        n = rd.randint(0, len(L0) - 1)
        L.append(L0[n])
        L0.pop(n)

    entrela(T, L)  # Redessine avec la nouvelle permutation
    root.mainloop()
    return True

# Fonction d’affichage principale
def affichage(T, n):
    c = ["black", 'red', "green", "blue"]
    entrela(T, c)

    # Bouton pour quitter la fenêtre
    bouton_quitter = tk.Button(root, text="Quitter", command=root.destroy)
    bouton_quitter.grid(row=1, column=0, sticky="W")

    # Bouton pour permuter les couleurs
    bouton_col = tk.Button(root, text="colors", command=permutcol)
    bouton_col.grid(row=1, column=0, sticky="E")

    root.mainloop()

# Liste de croisements à afficher
T = [2, 1, 1, 0, 2]
n = 4
affichage(T, n)
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 09:47:24 2025

@author: kylian
"""

# Importation des bibliothèques
import tkinter as tk
from tkinter import Tk, Label, Frame, Button
import numpy as np
import time

# Classe principale de l'application graphique
class App():
    def __init__(self,data):
        # Dimensions des éléments graphiques
        self.h = 40  # Hauteur d'un segment (vertical)
        self.w = 50  # Largeur d'un segment (horizontal)
        self.x0 = 10  # Décalage horizontal initial
        self.y0 = 25  # Décalage vertical initial
        self.D = data  # Données de l'entrelacement (objet Data)
        root = tk.Tk()  # Création de la fenêtre principale
        self.R = root
        self.canvas = 0  # Stocke le canvas actif
        self.time = 0  # Chronomètre
        self.tic = 100  # Pas de temps pour le timer (en ms)

    # Gère les clics souris pour supprimer des croisements
    def Tri(self, e):
        n = self.D.getfils()
        x = e.x
        y = e.y
        y0 = self.y0
        h = self.h
        w = self.w
        x0 = self.x0
        T = self.D.getentrela()
        k = 0
        L = []
        t = T[(x - x0) // (2 * w)]  # Indice de croisement cliqué
        p = (x - x0) // (2 * w)
        if y < y0 + h * n and y > y0 + h * t and x < x0 + w * 2 * len(T):
            for i in T[p:]:
                if i == t:
                    L.append(k)
                if i == t + 1 or i == t - 1:
                    L.append(-1)
                k += 1
            if len(L) > 1 and L[1] == -1:
                L[0] = -1
            L.append(-1)
            j = 0
            while L[j] != -1:
                T[p + L[j]] = -3  # Supprime le croisement
                j += 1
            self.D.changentrela(T)
            self.can()  # Redessine le canvas

    # Génère un nouvel entrelacement aléatoire
    def alea(self):
        import random as rd
        a = len(self.D.getcol())
        n = rd.randint(2, a)
        T = [rd.randint(0, n - 2) for i in range(rd.randint(2, 10))]
        self.D.changentrela(T)
        self.D.changefils(n)
        self.time = 0
        self.can()

    # Lance l'interface graphique
    def run_forever(self):
        root = self.R
        self.can()
        root.bind("<Button>", self.Tri)  # Active le clic souris

        # Boutons de l'interface
        bouton_quitter = tk.Button(root, text="Quitter", command=root.destroy)
        bouton_quitter.grid(row=1, column=0, sticky="W")

        bouton_col = tk.Button(root, text="colors", command=self.permcol)
        bouton_col.grid(row=1, column=0, sticky="E")

        bouton_new = tk.Button(root, text="new", command=self.alea)
        bouton_new.grid(row=1, column=0)

        # Affichage du chronomètre
        self.horloge = tk.Label(root, text=self.time)
        self.horloge.grid(row=0, column=1, sticky="s")
        self.horloge.after_idle(self.refresh)  # Démarre le timer

        root.mainloop()

    # Met à jour le chronomètre toutes les tic millisecondes
    def refresh(self):
        tic = self.tic
        horloge = self.horloge
        arrondi = round(self.time, 3)
        horloge.config(text=arrondi)
        self.time += tic / 1000
        T = self.D.getentrela()

        # Vérifie si tous les croisements sont supprimés
        if T == [-3 for i in range(len(T))]:
            print(f"Bravo! Tu as réussi en: {arrondi} s")
            self.time = 0
            horloge.after(tic, self.alea)  # Redémarre un nouvel entrelacement
        horloge.after(tic, self.refresh)

    def redraw(self):
        return True  # Fonction inutilisée ici

    # Affiche ou redessine le canvas avec l'entrelacement actuel
    def can(self):
        if self.canvas != 0:
            self.canvas.destroy()  # Supprime le canvas précédent

        root = self.R
        h = self.h
        w = self.w
        x0 = self.x0
        y0 = self.y0
        n = self.D.getfils()
        T = self.D.getentrela()
        c = self.D.getcol()
        L = [[x0, i * h + y0] for i in range(n)]  # Positions initiales des fils

        # Création d’un nouveau canvas
        canvas = tk.Canvas(root, width=w * (len(T) + 1) * 2, height=h * n + y0, bg="white")
        canvas.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        # Dessin des segments (croisements ou lignes droites)
        for i in T:
            for k in range(len(L)):
                y = L[k][1]
                x = L[k][0]
                canvas.create_line(x, y, x + w, y, fill=c[k], width=2)
                x += w

                if L[k][1] == i * h + y0:  # Fil descend
                    canvas.create_line(x, y, x + w, y + h, fill=c[k], width=2)
                    x += w
                    y += h
                elif L[k][1] == (i + 1) * h + y0:  # Fil monte
                    canvas.create_line(x, y, x + w, y - h, fill=c[k], width=2)
                    x += w
                    y -= h
                else:  # Ligne droite
                    canvas.create_line(x, y, x + w, y, fill=c[k], width=2)
                    x += w

                L[k] = [x, y]  # Mise à jour position

        # Derniers segments horizontaux
        for k in range(len(L)):
            y = L[k][1]
            x = L[k][0]
            canvas.create_line(x, y, x + w, y, fill=c[k], width=2)
            x += w
            L[k] = [x, y]

        # Affichage du texte avec l’état actuel
        canvas.create_text(w * (len(T) + 1), h * (n), text=f"croisement:  {T}", fill="black", font=("Arial", int(2 * np.log2(h)), "bold"))
        self.canvas = canvas  # Mémorise le canvas actif

    # Permute aléatoirement les couleurs
    def permcol(self):
        n = self.D.getfils()
        T = self.D.getentrela()
        c = self.D.getcol()
        import random as rd
        L0 = [i for i in c]
        L = []
        for i in range(len(L0)):
            n = rd.randint(0, len(L0) - 1)
            L.append(L0[n])
            L0.pop(n)
        self.D.changecol(L)
        self.can()  # Redessine avec les nouvelles couleurs

# Classe contenant les données de l'entrelacement et des couleurs
class Data:
    def __init__(self, fils, entrelacement):
        self.color = ["black", "red", "blue", "green", "orange", "purple", "brown"]
        self.fils = fils  # Nombre de fils
        self.entrela = entrelacement  # Liste des croisements

    def getcol(self):
        return self.color

    def getfils(self):
        return self.fils

    def getentrela(self):
        return self.entrela

    def changecol(self, col):
        self.color = col

    def changentrela(self, T):
        self.entrela = T

    def changefils(self, n):
        self.fils = n

# Lancement du programme
if __name__ == "__main__":
    data = Data(4, [2, 1, 1, 0, 2])
    app = App(data)
    app.run_forever()

# -*- coding: utf-8 -*-
"""
Created on Wed May 14 08:39:48 2025

@author: kylian
"""


import tkinter as tk
from tkinter import Tk, Label, Frame, Button
import numpy as np
import time
import random as rd




#exemple de dessin
def draw(can, graph, pos,root):
    X,Y=pos
    for i in range(len(graph)):
        x=X[i]
        y=Y[i]
        for j in graph[i]:  # sucs de i a j
            can.create_line(X[i],Y[i],X[j],Y[j])
        can.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")
    return can
    

def moov(X,Y,V,G,dt,dim):
    e=0.1
    k=1000
    a=0.1
    h=dim[0]
    w=dim[1]
    r0=50
    r0=r0/h
    for i in range(len(G)):
        vF=[0,0]
        for j in G[i]:
            r=((X[i]-X[j])**2+(Y[i]-Y[j])**2)**(1/2)
            x=[-(X[i]-X[j])/(r**2),-(Y[i]-Y[j])/(r**2)]
            r=r/h
            F= k*(r-r0)
            vF=[vF[0] + x[0]*F , vF[1] + x[1]*F]
            F=0
            #V[j]=[V[j][0]+dt*x[0]*F ,V[j][1]+dt*x[1]*F]
        for j in range(len(G)):
            if j!=i:
                r=((X[i]-X[j])**2+(Y[i]-Y[j])**2)**(1/2)
                x=[-(X[i]-X[j])/(r**2),-(Y[i]-Y[j])/(r**2)]
                r=r/h
                F= -e/(r**2)
                vF=[vF[0] + x[0]*F , vF[1] + x[1]*F]
        V[i]=[V[i][0]+dt*vF[0] - a*V[i][0],V[i][1]+dt*vF[1] - a*V[i][1]]
        if int(X[i])<=0:
            V[i][0]=abs(V[i][0])
        if int(X[i])>=w:
            V[i][0]=-abs(V[i][0])
        if int(Y[i])<=0:
            V[i][1]=abs(V[i][1])
        if int(Y[i])>=h:
            V[i][1]=-abs(V[i][1])
        
    for i in range(len(G)):
        X[i]=X[i]+V[i][0]
        Y[i]=Y[i]+V[i][1]
    return X,Y
                
def f():
    return True

def refresh(X,Y,V,G,dt,can,root,dim):
    w=dim[0]
    h=dim[1]
    can.destroy()
    
    can = tk.Canvas(root, width=w , height=h , bg="white")
    can.grid(row=0, column=0, padx=10, pady=10, sticky="n")
    X,Y=moov(X,Y,V,G,dt,dim)
    draw(can,G,(X,Y),root)
    

def cloc(H,dt,X,Y,V,G,can,root):
    H.after(int(dt*1000))
    #refresh(X,Y,V,G,dt,can,root,dim)
    
    

def animation(G):
    root = tk.Tk()  # Création de la fenêtre principale
    dim= (500,500)
    N=len(G)
    dt=1
    X=[rd.randint(20,dim[0]-20) for i in range(N)]
    Y=[rd.randint(20,dim[1]-20) for i in range(N)]
    V=[[0,0] for i in range(N)]
    w=dim[0]
    h=dim[1]
    
    can = tk.Canvas(root, width=w , height=h , bg="white")
    can.grid(row=0, column=0, padx=10, pady=10, sticky="n")
    can = draw(can,G,(X,Y),root)
    
    horloge = tk.Label(root, text=time)
    #cloc(horloge,dt,X,Y,V,G,can,root)
    root.bind("<f>",lambda e:refresh(X,Y,V,G,dt,can,root,dim))
    bouton_new = tk.Button(root, text="new",)
    bouton_new.grid(row=1, column=0)
    root.mainloop()
    
    """
    for i in range(100):
        horloge.after(int(dt*1000), refresh(X,Y,V,G,dt,can,root))
        
    """
        
        
        
        
    
        
    



graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
g2= [[2],[0,2],[0]]
g1=[[1],[0]]


animation(graph)
# -*- coding: utf-8 -*-
"""
Created on Wed May 28 09:46:47 2025

@author: kylian
"""
import random as rd
#Exo 1

class Poly:
    def __init__(self,p, q,n):
        self.q=q
        self.n=n
        self.p=p
    def __str__(self):
        return self.p
    def getn(self): #renvoi la valeur de n
        return self.n
    def getq(self): # renvoi la valeur de q
        return self.q
    def scale(self): # place le polynome dans le bon ensemble
        p=self.p
        n=self.n
        q=self.q
        k=len(p)
        while k>n:
            p[k-n-1]+=(-1)*p[k-1]
            p.pop()
            k-=1
        p= [i%q for i in p]
        self.p=p
        return self
    def mul(self,Q):
        p=self.p
        M=[0 for k in range(len(Q)+len(p))]
        for i in range(len(M)):
            for j in range(i+1):
                if i-j< len(Q) and j < len(p):
                    M[i]+=Q[i-j]*p[j]
        self.p=M
        self.scale()
        return self
    def add(self,Q): 
        p=self.p
        m=min(len(p),len(Q))
        S=[p[i]+Q[i] for i in range(m)]
        S=S+p[m:]+Q[m:]
        self.p=S
        self.scale()
        return self
    def scalar(self, c): # multipli les coefficients du polynome par c
        self.p=[(i*c)%self.q for i in self.p]
        return self.p
    def fscalar(self,r,alpha): #change le paramètre q et multipli les coefficients du polynome par alpha
        self.q=r
        self.p=[round(i*alpha)%self.q for i in self.p]
        return self
    def rescale(self, r): #change le paramètre q
        self.q=r
        self.scale()
        return self
    def copie(self): #fait une copie du polynome pour éviter les effet de bord 
        return Poly([i for i in self.p], self.q, self.n)
    
#Exo 2

def gen_uniform_random(q, n, a, b):
    L=[rd.randint(a,b)%q for i in range(n)]
    return L        

"""p=Poly([1,1,1],5,5)
a=[1,1,1]
print(p.__str__())
print(p.add(a))
print(p.mul(a))
print(p.scalar(4))
print(p.rescale(2))
print(gen_uniform_random(7, 6, 3, 8))"""
#%%
#Exo3
N=5
q2=30000
t=26
p=Poly(gen_uniform_random(t, N, 0, t-1),t,N)
a=Poly(gen_uniform_random(q2, N, 0, q2-1),q2,N)
sk=Poly(gen_uniform_random(2, N, 0, 1),q2,N)
E=[0,1,q2-1]
e=Poly([E[i] for i in gen_uniform_random(3,N,0,2) ],q2,N)
print("p:",p.__str__())
print("sk: ",sk.__str__(),"\ne" ,e.__str__())
def clee_public(a2,sk2,e3):
    poly=a2.copie()
    L=sk2.__str__()
    poly.mul(L)
    poly.add(e3.__str__())
    poly.scalar(-1)
    return poly

b=clee_public(a, sk, e)
print("a:", a.__str__(),"\nb:",b.__str__())

#%%
#Exo4

def chiffrement2(p,a2,b2,q,t,n):
    delta=q/t
    sp=p.copie().fscalar(q, delta)
    u=Poly(gen_uniform_random(q, n, 0, 1), q,n)
    e1= Poly(gen_uniform_random(q, n, -1, 1),q,n)
    c1=clee_public(b2,u,e1)
    c1.add(sp.__str__())
    e2=Poly(gen_uniform_random(q, n, -1, 1),q,n)
    c2=clee_public(a2,u,e2)
    #print("e1:",e1.__str__(),"\ne2:",e2.__str__(),"\na2:", a2.__str__(), "\nb2", b2.__str__())
    return (c1,c2)

(c1,c2)=chiffrement2(p, a, b, q2, t, N)
print("c1:",c1.__str__(),"\nc2",c2.__str__())

#%%
#Exo 5
p2=Poly(gen_uniform_random(t, N, 0, t-1),t,N)
(c3,c4)=chiffrement2(p2, a, b, q2, t, N)
print("valeurs de polynome de départ:","\np:",p.__str__(),"   p2:",p2.__str__(),"\n")

def dechiffre(k1,k2,sk,t):  #permet de dechiffrer le polynome chiffrés à partir de la méthode employé dans ce TD
    k2=k2.copie()
    k1=k1.copie()
    k2.mul(sk.__str__())
    k1.add(k2.__str__())
    k1.fscalar(t,t/k1.getq())
    return k1
pdech=dechiffre(c1,c2,sk,t)
print("p (déchiffrée à partir de c1 et c2):",pdech.__str__(),"\n")
som1,som2= c3.copie().add(c1.__str__()), c4.copie().add(c2.__str__())
somdech=dechiffre(som1,som2,sk,t)
print("som (déchiffrée):",somdech.__str__(),"\nsom (p+p2):",p.copie().add(p2.__str__()).__str__())

#%%
#Exo 6
""" Il faudrait trouvet une aplication bijective, tel que F(X*Y) = F(X)*F(Y)."""
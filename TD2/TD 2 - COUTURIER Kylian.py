# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 09:46:23 2025

@author: kylian
"""



#1. Objet polynome

class polynome:
    def __init__(self,P):
        self.poly=P    
    def __str__(self):
        P=self.poly
        s= f"{self.poly[0]}"
        for i in range(1,len(P)):
            if self.poly[i]!= 0:
                if i==1 :
                    s+=" + "
                    s=s+ f"{self.poly[i]}*X"
                else:
                    s+=" + "
                    s=s + f"{self.poly[i]}*X^{i}"
        print(s)
        return s

    def add(self,Q):
        P=self.poly
        R=[0 for i in range(max(len(P),len(Q)))]
        for i in range(min(len(P),len(Q))):
            R[i]= P[i]+Q[i]
        if i== len(P)-1 and len(P)!=len(Q):
            R+=Q[i:len(Q)]
        if i==len(Q)-1 and len(P)!=len(Q):
            R+=P[i:len(Q)]
        self.poly=R
        self.__str__()
        
           
            
    
if __name__=="__main__":
    p=polynome([1,2,3]) #création du polyome
    assert(type(p.__str__()) == str)
    p.__str__()
    p.add([1,1,1])
    
#%%
class polynome_mod:
    #exercice 2:
    
    def __init__(self,P,n,q):
        self.poly=P
        self.deg=n
        self.coef=q    
    def __str__(self):
        P=self.poly
        s= f"{self.poly[0]}"
        for i in range(1,len(P)):
            if self.poly[i]!= 0:
                if i==1 :
                    s+=" + "
                    s=s+ f"{self.poly[i]}*X"
                else:
                    s+=" + "
                    s=s + f"{self.poly[i]}*X^{i}"
        return s
    
    def modulo(self):
        n=self.deg
        q=self.coef
        P=self.poly
        m=len(P)
        for i in range(len(P)):
            a=m-1-i
            if a>=n:
                a-=n
                P[a]-=P[a+n]
                P.pop()
            if abs(P[a]) >=q:
                P[a]= P[a]%q
            if P[a]<0:
                P[a]+=q
        self.poly=P
        return P
    #Exercice 3:
    
    def scalar(self, c): # c * self
        P=[c*i for i in self.poly]
        self.poly=P
        self.modulo()
        return self.poly
    
    def rescale(self, r):
        self.coef=r
        self.modulo()
        return self.poly
    
    #Exercie 4:
    
    def add(self,Q):
        P=self.poly
        R=[]
        for i in range(min(len(P),len(Q))):
            R[i]= P[i]+Q[i]
            if i== len(P)-1 and len(P)!=len(Q):
                R+=Q[i:len(Q)]
            if i==len(Q)-1 and len(P)!=len(Q):
                R+=P[i:len(Q)]
        R.modulo(self)
        
    #♦Exercie 5:
    
    def mul(self,Q):
        P=self.poly
        R=[0 for i in range(len(P) + len(Q)-1)]
        for i in range(len(Q)):
            for j in range(len(P)):
                R[i+j]+= P[j]*Q[i]
        self.poly=R
        return self.modulo()

if __name__=="__main__":
    p=polynome_mod([1,2,3,4],3,5)
    assert(type(p.__str__()) == str)
    print(p.__str__())
    print(p.modulo())
    print(p.scalar(2))
    print(p.mul([3]))
    print(p.rescale(3))
    print(p.__str__())
        

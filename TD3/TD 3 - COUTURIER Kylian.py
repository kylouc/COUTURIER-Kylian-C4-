# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 09:10:45 2025

@author: kylian
"""

#%% Exercice 1

"""

"""




#%% Exercice 2

class Tree:
    def __init__(self, symbol, *children): 
        self.__symbol = symbol
        self.__children = children
        
    def label(self):#str
        return self.__symbol
    
    def children(self): # tuple[Tree]
        return self.__children 
    
    def nb_children(self): #int
        return len(self.__children)
    def child(self, i: int): #Tree
        return self.__children[i]
    def is_leaf(self): #bool
        return len(self.__children)==0
    def depth(self):
        def dep(n,c):
            if len(c)==0:
                return n
            else:
                c=c.children()
                return max(dep(n+1,i) for i in c)
        n=0
        c=self.__children
        return dep(0,c)
            
        

t=Tree('f',Tree('a'),Tree("b"))
print(t.children())

import unittest

class test_tree(unittest.TestCase):
    def __init__(self,tree): 
        self.t=tree
    def test_label(self):#str
        l=t.label()
        self.assertTrue(type(l)==str)
    def test_children(self): # tuple[Tree]
        c=t.children()
        self.assertTrue(type(c)==tuple)
    def test_nb_children(self): #int
        nb_ch=t.nb_children()
        self.assertTrue(type(nb_ch)==int)
    def test_child(self, i: int): #Tree
        child=t.child(i)
        self.assertTrue(type(child)==tuple)
        return self.__children[i]
    def test_is_leaf(self): #bool
        isleaf=t.is_leaf()
        self.assertTrue(type(isleaf)==bool)
    def test_type(self):
        l=t.label()
        self.assertTrue(type(l)==str)
        c=t.children()
        self.assertTrue(type(c)==tuple)
        nb_ch=t.nb_children()
        self.assertTrue(type(nb_ch)==int)
        isleaf=t.is_leaf()
        self.assertTrue(type(isleaf)==bool)
    
t=Tree('f',Tree('a'),Tree("b"))
u=test_tree(t)
#print(u.test_type())




#%% Exercice 3


class Tree:
    def __init__(self, symbol, *children): 
        self.__symbol = symbol
        self.__children = children
        
    def label(self):#str
        return self.__symbol
    
    def children(self): # tuple[Tree]
        return self.__children 
    
    def nb_children(self): #int
        return len(self.__children)
    def child(self, i: int): #Tree
        return self.__children[i]
    def is_leaf(self): #bool
        return len(self.__children)==0
    def depth(self):
        if self.is_leaf():
            return 0
        else:
            return 1 + max(child.depth() for child in self.children())

t=Tree('f',Tree('a'),Tree("b"))
print(t.depth())

#%% Exercice 4


class Tree:
    def __init__(self, symbol, *children): 
        self.__symbol = symbol
        self.__children = children
        
    def label(self):#str
        return self.__symbol
    
    def children(self): # tuple[Tree]
        return self.__children 
    
    def nb_children(self): #int
        return len(self.__children)
    def child(self, i: int): #Tree
        return self.__children[i]
    def is_leaf(self): #bool
        return len(self.__children)==0
    def depth(self):
        if self.is_leaf():
            return 0
        else:
            return 1 + max(child.depth() for child in self.children())
    
    def __str__(self) -> str:
        operation={"/","*","-","+",".","%","//"}
        if self.is_leaf():
            return self.label()
        else:
            if self.label() not in operation:
                s=f"{self.label()}("
                n=0
                for child in self.children():
                    n+=1
                    s+=child.__str__()
                    if n!= len(self.children()):
                        s+=", "
                s+=")"
            else:
                n=0
                s=""
                for child in self.children():
                    n+=1
                    s+=child.__str__()
                    if n!= len(self.children()):
                        s+=f" {self.label()} "
            return s
    def __eq__(self, __value: object) -> bool:
        return self.__str__()== __value.__str__()
    #def deriv(self, var: str): #[Tree]
        
    
        

t=Tree('f',Tree('a'),Tree("b"))
print(t.__str__())

#ATTENTION: Il manque les tests.



#%% Exercice 5


class Tree:
    def __init__(self, symbol, *children): 
        self.__symbol = symbol
        self.__children = children
        
    def label(self):#str
        return self.__symbol
    
    def children(self): # tuple[Tree]
        return self.__children 
    
    def nb_children(self): #int
        return len(self.__children)
    def child(self, i: int): #Tree
        return self.__children[i]
    def is_leaf(self): #bool
        return len(self.__children)==0
    def depth(self):
        if self.is_leaf():
            return 0
        else:
            return 1 + max(child.depth() for child in self.children())
    def __str__(self) -> str:
        operation={"/","*","-","+",".","%","//","^"}
        if self.is_leaf():
            return self.label()
        else:
            if self.label() not in operation:
                s=f"{self.label()}("
                n=0
                for child in self.children():
                    n+=1
                    s+=child.__str__()
                    if n!= len(self.children()):
                        s+=", "
                s+=")"
            else:
                n=0
                s=""
                for child in self.children():
                    n+=1
                    s+=child.__str__()
                    if n!= len(self.children()):
                        s+=f" {self.label()} "
            return s
    def __eq__(self, __value: object) -> bool:
        return self.__str__()== __value.__str__()
    def deriv(self, var: str): #[Tree]    
        if self.label()=="+":
            return Tree("+", *[child.deriv(var) for child in self.children() if child.deriv(var)!= None])
        if self.label()=="*":
            n=0
            L=[]
            for child in self.children():
                if child.__eq__(Tree(var)):
                    n+=1
                else:
                    L.append(child)
            if n==0:
                return None
            if n ==1:
                return Tree("*", *L)           
            L=[n]+L+[Tree(var) for i in range(n-1)]
            return Tree("*", *L)
        if self.__eq__(Tree(var)):
            return Tree("1")
        else:
            return None

            

t=Tree("+", Tree("*",Tree('3'),Tree("X"),Tree('X')),Tree("*",Tree('5'),Tree("X")),Tree("7"))
t2=t.deriv("X")
print(t2.__str__())



#%% Exercice 6







#%% Exercice 7






#%% Exercice 8




#%% Exercice 9






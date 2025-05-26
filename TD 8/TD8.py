# -*- coding: utf-8 -*-
"""
Created on Wed May 21 09:44:57 2025

@author: kylian
"""
#Exercice 1
from struct import unpack_from, pack
f = open("the_wall.wav", "rb")
datastart = f.read(44)
data=f.read()
s=[[], []]
n=(len(data))//4  -2
for i in range(n):
    left=unpack_from("<h",data,4*i)[0]
    right=unpack_from("<h",data,4*i+2)[0]
    s[0].append(left)
    s[1].append(right)
import matplotlib.pyplot as plt
l=250
T= [i for i in range(len(s[0][:l]))]
plt.plot(T, s[1][:l], color='red')
plt.plot(T, s[0][:l], color='blue')

#plt.show()
print(datastart)
print(len(data))
for i in range(len(datastart)):
    print(unpack_from("I",datastart,i)[0])


#%% Exercice 2
f = open("the_wall.wav", "rb")
datastart = f.read(44)
data=f.read()
s=[[], []]
n=(len(data))//4  -2
for i in range(n):
    left=unpack_from("<h",data,4*i)[0]
    right=unpack_from("<h",data,4*i+2)[0]
    s[0].append(left)
    s[1].append(right)

with open("invers.wav", "wb") as g:
    g.write(datastart)
    for i in range(len(s[0])):
        p=pack("<h",s[0][len(s[0])-i-1])
        p2=pack("<h",s[1][len(s[1])-i-1])
        g.write(p)
        g.write(p2)
    for i in range(len(s[0])):
        p=pack("<h",s[0][len(s[0])-i-1])
        p2=pack("<h",s[1][len(s[1])-i-1])
        g.write(p)
        g.write(p2)
    
#%% Exercice 3    
f = open("the_wall.wav", "rb")
datastart = f.read(44)
data=f.read()
s=[[], []]
n=(len(data))//4  -2
for i in range(n):
    left=unpack_from("<h",data,4*i)[0]
    right=unpack_from("<h",data,4*i+2)[0]
    s[0].append(left)
    s[1].append(right)   
 
with open("x2.wav", "wb") as g:
    g.write(datastart)
    for i in range(len(s[0])//2-1):
        p=pack("<h",s[0][i*2])
        p2=pack("<h",s[1][i*2+1])
        g.write(p)
        g.write(p2)

#%% Exercice 4
f = open("the_wall.wav", "rb")
datastart = f.read(44)
data=f.read()
s=[[], []]
n=(len(data))//4  -2
for i in range(n):
    left=unpack_from("<h",data,4*i)[0]
    right=unpack_from("<h",data,4*i+2)[0]
    s[0].append(left)
    s[1].append(right)


new_data_size = (len(s[0]) - 1) * 4*2
datastart = bytearray(datastart)
datastart[4:8] = pack("<I", 36 + new_data_size)      # ChunkSize
datastart[40:44] = pack("<I", new_data_size) 

        
with open("interpol.wav", "wb") as g:
    g.write(datastart)
    for i in range(len(s[0])-1):
        p=pack("<h",s[0][i])
        p2=pack("<h",s[1][i])
        p3=pack("<h",(s[0][i+1]+s[0][i+1])//2)
        p4=pack("<h",(s[1][i+1]+s[1][i+1])//2)
        g.write(p)
        g.write(p2)
        g.write(p3)
        g.write(p4)
    
#%% Exercice 5



#%% Exercice 6
from struct import unpack_from, pack
f = open("the_wall.wav", "rb")
datastart = f.read(44)
data=f.read()
s=[[], []]
n=(len(data))//4  -2
for i in range(n):
    left=unpack_from("<h",data,4*i)[0]
    right=unpack_from("<h",data,4*i+2)[0]
    s[0].append(left)
    s[1].append(right)

delay=1 #seconde
r=1 #absorbtion du sons
freq=44100
with open("echo.wav", "wb") as g:
    g.write(datastart)
    for i in range(len(s[0])):
        if i >delay*freq:
            s[0][i]=s[0][i]+ (s[0][int(i-delay*freq)])*r
            s[1][i]=s[1][i] + (s[1][int(i-delay*freq)])*r
        if abs(s[0][i])>32767:
            s[0][i]=int(32766*(s[0][i]/abs(s[0][i])))
        if abs(s[1][i])>32767:
            s[1][i]=int(32766*(s[1][i]/abs(s[1][i])))
        p=pack("<h",int(s[0][i]))
        p2=pack("<h",int(s[1][i]))
        g.write(p)
        g.write(p2)
    

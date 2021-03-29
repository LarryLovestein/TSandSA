import numpy as np
from math import *
from UI import scrieFisier,scrieSA

def generareRandom(n):
    pozitii = np.random.randint(2, size=n)
    return pozitii


def verificareGhiozdan(listgrval, greutateGhiozdan, pozitii):
    suma = 0
    for i in range(0, len(pozitii)):
        suma = suma + int(pozitii[i]) * (listgrval[i][0])
    if suma <= greutateGhiozdan:
        return suma
    else:
        return -1


def generareSolVal(n, listgrval, greutateGhiozdan):
    while True:
        pozitii = generareRandom(int(n))
        if verificareGhiozdan(listgrval, greutateGhiozdan, pozitii) != -1:
            return pozitii


def detValoare(pozitii, listgrval):
    valoarea=0
    for i in range(0, len(pozitii)):
        valoarea=valoarea+int(pozitii[i]*listgrval[i][1])
    return valoarea

def valMaxima(valori):
    maxim1=0
    grmaxim=0
    for i in range(0,len(valori)):
        if valori[i][0] > maxim1:
            maxim1= valori[i][0]
            grmaxim= valori[i][1]
    return maxim1,grmaxim

def avgTabu(valori):
    suma=0
    for i in range(0,len(valori)):
        suma += int(valori[i][0])
    return suma/len(valori)





def bestNeighbourNonTabu(c, istoric, listgrval, greutateGhiozdan):  # c ii vector de pozitii
    pozitia = -1
    bestN = [0] * len(c)  # facem un vector bestN cu len(c) 0-uri care reprezinta best vecin
    for i in range(0, len(c)): #parcurgem fiecare bit din c
        copyC = c.copy()       # facem o copie la c
        if istoric[i] != 0:     # daca pozitia este tabu merge mai departe
            continue
        else:                   #daca nu e tabu atunci:
            copyC[i]=1-copyC[i]   #daca copie[i]=0 il face 1 si invers
            if verificareGhiozdan(listgrval,greutateGhiozdan,copyC)> verificareGhiozdan(listgrval,greutateGhiozdan,bestN):
                bestN=copyC.copy()      #comparam pe rand fiecare vecin non tabu si daca este mai bun decat cel precedent atunci el devine best
                pozitia=i
    return bestN,pozitia    #returneaza cel mai bun vecin non tabu si pozitia pe care se afla bitul schimbat






def updateIstoric(nrItrTabu, poz, istoric):

    for i in range(0,len(istoric)): #parcurgem istoricul
        if int(istoric[i]) > 0:      #daca pe pozitia respectiva valoarea este mai mare decat 0 atunci scadem o valoare
            istoric[i] = int(istoric[i])-1
    istoric[poz]=int(nrItrTabu)        # dupa ce am modificat toate valorile ce trebuia modificate am pus pe pozitia coresp nrItrTabu(pozitia este data
                                      # de bestNeighbourNonTabu
    return istoric



def tabuSearch(listgrval, greutateGhiozdan, nrIter, nrItrTabu, n, k):
    j=0
    while j < int(k):
        c = generareSolVal(n, listgrval, greutateGhiozdan)  #generare solutie valida
        #print("punctul de pornire",c)
        best = c.copy()     #se face o copie la solutia generata
        istoric = [0] * len(listgrval)  # se initializeaza vectorul Istoric cu 0
        i = 0
        while i < int(nrIter):
            x,poz = bestNeighbourNonTabu(c, istoric, listgrval, greutateGhiozdan)  # se ia cel ami bun vecin nontabu si pozitia lui
            #print(x)
            istoric=updateIstoric(nrItrTabu, poz, istoric)  #update istoric
            c=x.copy()         #c devine x
            #print(c)
            #print("istoric: ",istoric)
            if detValoare(best,listgrval) < detValoare(c,listgrval): #daca valoarea vecinului este mai buna decat best-ul atunci best devine vecinul
                best=c.copy()
            i += 1
        #print(best)
        valoarea=detValoare(best,listgrval)         #determinam valoarea best-ului la sfarsit
        #print(valoarea)
        greutate=verificareGhiozdan(listgrval,greutateGhiozdan,best) #det greutatea best-ului
        scrieFisier("tabu.txt",j,valoarea,greutate) #il scriem in fisier
        j += 1
    return best #il returnam

def distEuclidiana(punctA, punctB):
    return int(sqrt(pow((punctB[0]-punctA[0]),2)+ pow((punctB[1]-punctA[1]),2)))


import random


def solinitialaTsp(n):
    randomlist = random.sample(range(1, int(n)+1), int(n))
    return randomlist

'''

input: o lista cu valori de la 1 la n puse random
Genereaza 2 valori random intre 0 si n-1 care reprezinta indecsi cu care se vor face swipe
output: se returneaza o copie a vectorul modificat
'''
def generareVecinTsp(solinitTsp):
    randomtwo= random.sample(range(0,len(solinitTsp)), 2)
    copie=solinitTsp.copy()
    copie[randomtwo[0]], copie[randomtwo[1]] = copie[randomtwo[1]], copie[randomtwo[0]]
    return copie

def memorieDistante(listaPct):
    matrice=[[0]*len(listaPct)]*len(listaPct)
    for i in range(len(listaPct)):
        val=[0]*len(listaPct)
        for j in range(i,len(listaPct)):
            val[j]=distEuclidiana(listaPct[i],listaPct[j])
            matrice[i]=val.copy()
    return matrice



'''
input: o lista cu valori de la  1-n random puse si o matrice superioara ce are valorile distantei euclidiane dintre pct
Face o suma cu distantele dintre orase in functie de ordinea lor in lista
output: Un numar intreg ce reprezinta valoarea drumului total prin toate orasele + intoarcerea in orasul initial 

'''


def evalTsp(lista, matrice):
    suma=0
    for i in range(len(lista)):
        j=i+1
        if j == len(lista):
            if lista[0] > lista[i]:
                suma=suma+matrice[lista[i]-1][lista[0]-1]
            else:
                suma=suma+matrice[lista[0]-1][lista[i]-1]
            return suma
        if lista[i] > lista[j]:
            suma=suma+matrice[lista[j]-1][lista[i]-1]
        else:
            suma = suma + matrice[lista[i]-1][lista[j]-1]




import math
'''
Input:k-nr sol generate,T-temperatura initiala, alpha- gradul de racire,minT-temperatura minimia
     nrIter-numarul maxim de iteratii, matrice- matricea cu distantele dintre fiecare oras
Output: returneaza lista drumului mai buna si valoarea acestuia
'''
def simulatedAnnealing(k, nrIter, matrice,T,alpha,minT):
    i=0
    while i < int(k):
        lista=solinitialaTsp(len(matrice[0]))
        #print("Solutia initiala:", evalTsp(lista,matrice))
        while T > minT:
            j = 0
            while j < int(nrIter):
                x=generareVecinTsp(lista)
                delta=evalTsp(x,matrice) - evalTsp(lista,matrice)
                if delta < 0:
                    lista=x.copy()
                else:
                    #print(math.exp(-delta/T))
                    if random.uniform(0,1) < math.exp(-delta/T):
                        lista=x.copy()
                j+=1
            #print(T)
            T=alpha*T
        #print(lista)
        scrieSA("SA.txt",lista,evalTsp(lista,matrice))
        #print("solutia imbunatatita:",evalTsp(lista,matrice))
        i += 1

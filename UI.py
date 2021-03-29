def afisareMeniu():
    print("0.Exit\n"
          "1.Citire de la tastatura\n"
          "2.Citire din fisier\n"
          "3.Citire Tabu Search\n"
          "4.Afisare lista puncte si matrice distante\n"
          "5.TSP\n"
          "6.Plotare Tabu Search\n"
          "7.Plotare TSP\n"
          )

def citireTastatura(n):
    listgrval=list()#o lista de tuple (greutate, valoare)
    for i in range(int(n)):
        greutate = int(input("Greutate: "))
        valoare = int(input("Valoare: "))
        listgrval.append((greutate,valoare))
    return listgrval

def citireFisier(numefis):
    listgrval=list()#o lista de tuple (greutate, valoare)
    f=open(numefis,"r")
    n=int(f.readline())
    for i in range(n):
        line=f.readline()
        listgrval.append((int(line.split()[1]),int(line.split()[2])))
    greutateGhiozdan=int(f.readline())
    f.close()
    return n, listgrval,greutateGhiozdan # n=nr de el, listgrval(tuplu de greutate si valoare)
def scrieFisier(numefis,nrIteratiei,valoarea, greutate):
    f = open(numefis, "a")
    f.write(str(nrIteratiei) + " " + str(valoarea) + " " + str(greutate) + "\n")
    f.close()

def citireTabu(numefis):
    f=open(numefis,"r")
    listgrval=list()
    while True:
        line = f.readline()
        if not line:
            break
        listgrval.append((int(line.split()[1]),int(line.split()[2])))
    f.close()
    return listgrval


def scrieSA(numefis,lista, valoarea):
    f=open(numefis,"a")
    f.write(str(lista) + " " + str(valoarea)  + "\n")
    f.close()

def readSA(numefis):
    f = open(numefis, "r")
    listgrval = list()
    while True:
        line = f.readline()
        if not line:
            break
        listgrval.append(int(line.split("]")[1]))
    f.close()
    return listgrval
import re
'''
x=readSA("SA.txt")
print(x.index(min(x)))
f=open("SA.txt","r")
line=f.readline()
print(re.split(' |, |]|\[',line))
'''
def readSAvect(numefis, linia):
    f=open(numefis,"r")
    listgrval = list()
    i=0
    while True:
        line = f.readline()
        if not line:
            break
        i+=1
        if linia==i:
            linie=re.split(' |, |]|\[',line)
            for j in range(1,len(linie)-2):
                listgrval.append(int(linie[j]))

    f.close()
    return listgrval

print(readSAvect("SA.txt",2))
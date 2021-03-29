
from UI import *
from Logic import *
import time
import matplotlib.pyplot as plt

'''
def pritnas():
    
    #n, listgrval, grGhiozdan = citireFisier("cazul20.txt")

    listgrval=[(1, 1), (3, 3), (4, 4), (5, 5), (10, 10)]
    n=len(listgrval)
    grGhiozdan=17
    istoric=[0, 0, 0, 1, 1]
    c=[1,0,0,1,1]
    x,poz=bestNeighbourNonTabu(c, istoric, listgrval, grGhiozdan)
    print(c)
    print(x)
    print(verificareGhiozdan(listgrval,grGhiozdan,x))
    print(detValoare(x,listgrval))

pritnas()
'''
def principal():


    while True:
        afisareMeniu()
        x = input("Introdu numarul corespunzaotr: ")
        if(x == "1"):
            grGhiozdan=int(input("greutatea ghiozdanului"))
            n=int(input("Numarul de elemente:"))
            print("Citeste lista de greutati si valori")
            listgrval=citireTastatura(n)
        if (x == "2"):
            numfis=input("numele fisierului")
            n, listgrval,grGhiozdan=citireFisier(numfis)

        if (x == "3"):



            k=input("nr de sol generate")
            nrIter = input("nr iteratii")
            nrItrTabu = input("nr iteratii tabu")
            i=0
            f = open("Best.txt", "w")
            f.write("")
            f.close()
            nrRulari=input("numar de rulari: ")
            start_time = time.time()
            while i<int(nrRulari):
                f = open("tabu.txt", "w")
                f.write("")
                f.close()
                tabuSearch(listgrval, grGhiozdan, nrIter, nrItrTabu, n,k)
                valori=citireTabu("tabu.txt")
                print(avgTabu(valori))
                #print(valMaxima(valori))
                valmax,grmax=valMaxima(valori)
                f=open("Best.txt","a")
                f.write(str(valMaxima(valori)[0])+" "+str(valMaxima(valori)[1]) +"\n")
                f.close()
                i+=1

            print("--- %s seconds ---" % (time.time() - start_time))
        if x=="4":
            start_time = time.time()
            print(listgrval)
            matrice=memorieDistante(listgrval)
            for i in matrice:
                print(i)
            lista=solinitialaTsp(len(listgrval))
            print(lista)
            print(evalTsp(lista,matrice))
            vecin=generareVecinTsp(lista)
            print("vecinul este: ",vecin)
            print(evalTsp(vecin,matrice))
            print("--- %s seconds ---" % (time.time() - start_time))
        if x=="5":
            f = open("bestSA.txt", "w")
            f.write("")
            f.close()
            k=input("Numarul de solutii generate")
            nrIter=input("Numarul maxim de iteratii")
            T = float(input("T-temperatura maxima:"))
            Alpha = float(input("Alpha:"))
            minT = float(input("minT:"))

            nrRulari=input("numarul de rulari:")
            i=0
            start_time = time.time()
            while i<int(nrRulari):
                f = open("SA.txt", "w")
                f.write("")
                f.close()
                simulatedAnnealing(k,nrIter,matrice,T,Alpha,minT)
                x=readSA("SA.txt")
                minim=min(x)
                pozMin=x.index(min(x))+1
                vectMIN=readSAvect("SA.txt",pozMin)
                scrieSA("bestSA.txt",vectMIN, minim)
                i+=1
            print("--- %s seconds ---" % (time.time() - start_time))
            print(readSA("bestSA.txt"))

        if x== "6":

            plt.title("Val. din " + numfis + " cu k= " + str(k) + " nr sol generate ")
            for i in range(len(valori)):
                plt.scatter(int(valori[i][0]), int(valori[i][1]), s=70, alpha=0.3)
            plt.plot(valmax, grmax, "ro", label="Valoare Maxima")
            plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', numpoints=1)
            plt.tight_layout()
            plt.ylabel('Greutatea')
            plt.xlabel('Valorile')
            plt.show()
            print(nrIter)
            print(nrItrTabu)
        if x=="7":
            x = readSA("bestSA.txt")
            minim = min(x)
            pozMin = x.index(min(x)) + 1
            vectMIN = readSAvect("bestSA.txt", pozMin)
            print(minim)
            print(vectMIN)
            print(np.mean(x))
            plt.title("Val. din " + " cu k= " + str(k) + " nr sol generate ")
            for i in vectMIN:
                plt.plot(int(listgrval[i-1][0]),int(listgrval[i-1][1]) ,linewidth = 3,marker='o', markerfacecolor='blue', markersize=4)
            vx=list()
            vy=list()
            for i in range(len(vectMIN)):
                j=i+1
                if j== len(vectMIN):
                    vx.append(listgrval[vectMIN[i] - 1][0])
                    vy.append(listgrval[vectMIN[i] - 1][1])
                    vx.append(listgrval[vectMIN[0]-1][0])
                    vy.append(listgrval[vectMIN[0]-1][1])
                    plt.plot(vx,vy,":")
                    break
                vx.append(listgrval[vectMIN[i]-1][0])
                vy.append(listgrval[vectMIN[i]-1][1])
                plt.plot(vx, vy, ":")
            plt.ylabel('Y-label')
            plt.xlabel('X-label')
            plt.show()
            print(evalTsp(vectMIN,matrice))
            print(listgrval)
        if(x == "0"):
            break
    print("codul s-a terminat cu succes")



principal()

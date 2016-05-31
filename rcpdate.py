#!/usr/bin/python

from random import randint


degrade = True



tempsMin = 10000
tempsMax = 0

tempsMoy = 0


tempsMinE = 10000
tempsMaxE = 0

tempsMoyE = 0

bornesDP = [(8,15),(4,18),(5,19),(4,9),(4,13),(5,13),(2,12),(4,6),(3,5),(5,8),(2,5),(3,19),(4,9)]
bornesDE = [(8,15),(4,18),(4,11),(0,0),(3,9),(5,13),(2,5),(0,0),(0,0),(0,0),(0,0),(3,19),(0,0)]


if degrade :
    bornesDP = [(8,15),(4,18),(5,19),(0,0),(0,0),(5,13),(0,0),(4,6),(3,5),(5,8),(2,5),(3,19),(4,9)]
    bornesDE = [(8,15),(4,18),(4,11),(0,0),(0,0),(5,13),(0,0),(0,0),(0,0),(0,0),(0,0),(3,19),(0,0)]



cible = 40

prob = 0
probE = 0


iterations = 1000
for k in range(iterations):

    delai = ['']*13

    delaiE = ['']*13


    for i in range(len(delai)):
        delai[i] = randint(bornesDP[i][0],bornesDP[i][1])

    for i in range(len(delaiE)):
        delaiE[i] = randint(bornesDE[i][0],bornesDE[i][1])



    delai1 = max(delai[0],delai[1],delai[2])

    delai2 = max(delai[4],delai[5],delai[6])

    delai3 = max(delai[9],delai[10],delai[12],delai[11])

    delai4 = max(delai[3],delai[7],delai[8])

    delaiFin = max(delai1+delai2+delai3,delai1+delai4)

    if delaiFin > tempsMax :
        tempsMax = delaiFin
    if delaiFin < tempsMin :
        tempsMin = delaiFin

    tempsMoy +=delaiFin

    if delaiFin <= cible :
        prob += 1


    delai1E = max(delaiE[0],delaiE[1],delaiE[2])

    delai2E = max(delaiE[4],delaiE[5],delaiE[6])

    delai3E = max(delaiE[9],delaiE[10],delaiE[12],delaiE[11])

    delai4E = max(delaiE[3],delaiE[7],delaiE[8])

    delaiFinE = max(delai1E+delai2E+delai3E,delai1E+delai4E)

    if delaiFinE > tempsMaxE :
        tempsMaxE = delaiFinE
    if delaiFinE < tempsMinE :
        tempsMinE = delaiFinE

    tempsMoyE +=delaiFinE

    if delaiFinE <= cible :
        probE += 1




if degrade :
    print "Mode degrade : \n"

print

print "Papier"
print "Temps minimum " +  str(tempsMin)
print "Temps Maximum " + str(tempsMax)
print "Temps Moyen "+ str(tempsMoy/iterations)
print "Probabilite "+ str(prob/float(iterations))

print "\nElectronique"
print "Temps minimum " +  str(tempsMinE)
print "Temps Maximum " + str(tempsMaxE)
print "Temps Moyen "+ str(tempsMoyE/iterations)
print "Probabilite "+ str(probE/float(iterations))
#!/usr/bin/python
__author__ = 'warreee'

from Cirkel import Cirkel
from BST import searchtree
def main():
    readInput()

#Deze methode leest het input bestand en verwacht de naam: cirkles.txt



def readInput():

    try:
        file = open('cirkels.txt')
    except:
        print("Het invoerbestand cirkels.txt werd niet gevonden!")
    else:
        algo = 0
        aantalCirkels = 0
        lijst = searchtree()
        for line in file:
            if algo == 0:
                algo = int(line)
            elif aantalCirkels == 0:
                aantalCirkels = int(line)
            else:
                #Gebruik het eerste algoritme
                if algo == 1:
                    print("test")
                else:
                    #Algoritme 2 of 3
                    str = line.strip().split(' ')
                    xco = int(str[0])
                    yco = int(str[1])
                    r = int(str[2])
                    lijst.insert(Cirkel(xco, yco, r))
if __name__ == "__main__": main()
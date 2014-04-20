#!/usr/bin/python
__author__ = 'warreee'

import Cirkel

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
        for line in file:
            if algo == 0:
                algo = line
            elif aantalCirkels == 0:
                aantalCirkels = line
            else:
                #maakt een nieuwe cirkel aan in de lijst
                str = line.split(' ')
                cirkel = Cirkel.Cirkel(str[0],str[1],str[2])

if __name__ == "__main__": main()
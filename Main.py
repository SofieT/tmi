#!/usr/bin/python
__author__ = 'warreee'

from Cirkel import Cirkel
#from BST import searchtree
from algo1 import algo1
from time import time

def main():
    algo, aantal_cirkels, lijst = readInput()

    if algo == 1:
        algorithm = algo1(lijst)
    elif algo == 2:
        pass
    elif algo == 3:
        pass
    else:
        print("Onbekend algoritme.")

    start = time()
    algorithm.execute()
    end = time()
    save_output(algorithm.get_intersections(), int((end - start) * 1000), True)

#Deze methode leest het input bestand en verwacht de naam: cirkles.txt



def readInput():

    lijst = list()
    try:
        with open('cirkels.txt', 'r') as file:
            algo = int(file.readline())
            aantalCirkels = int(file.readline())

            for line in file:
                temp = line.strip().split(' ')
                lijst.append(Cirkel(float(temp[0]), float(temp[1]), float(temp[2])))
    except:
        print('Kan de file "cirkels.txt" niet openen.')

    return algo, aantalCirkels, lijst


def save_output(list, execution_time, implemented):
    with open('output.txt', 'w') as f:
        if not implemented:
            f.write("")
            return

        for l in list:
            f.write(str(l[0]) + " " + str(l[1]) + "\n")
        f.write("\n")
        f.write(str(execution_time))
if __name__ == "__main__": main()
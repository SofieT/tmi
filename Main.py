__author__ = 'warreee'

def main():
    readInput()

#Deze methode leest het input bestand en verwacht de naam: cirkles.txt

def readInput():
    try:
        file = open('cirkels.txt')
    except:
        print("Het invoerbestand cirkels.txt werd niet gevonden!")


if __name__ == "__main__": main()
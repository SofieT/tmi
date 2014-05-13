from random import random
from Cirkel import Cirkel


def generate_cirkels(amount):

    cirkels = list()

    for a in range(amount):
        cirkels.append(Cirkel(random()*100, random()*100, random()*5))

    return cirkels


def write_to_file(cirkels):

    with open('cirkels.txt', 'w') as f:
        f.write("3\n")
        f.write(str(len(cirkels)))
        f.write('\n')

        for c in cirkels:
            f.write(str(c.getXco()) + " ")
            f.write(str(c.getYco()) + " ")
            f.write(str(c.getR()) + "\n")


c = generate_cirkels(100)


write_to_file(c)



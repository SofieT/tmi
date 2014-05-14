from random import random
from Cirkel import Cirkel


def generate_cirkels(amount):

    cirkels = list()

    for a in range(amount):

<<<<<<< HEAD
        cirkels.append(Cirkel(1*random(), 1*random(), 1*random()))
=======
        cirkels.append(Cirkel(1*random(), 1*random(), 0.1*random()))
>>>>>>> b860020a56a88862d46286c28075ac8c69b4f441



    return cirkels


def write_to_file(cirkels):

    with open('input.txt', 'w') as f:
        f.write("3\n")
        f.write(str(len(cirkels)))
        f.write('\n')

        for c in cirkels:
            f.write(str(c.getXco()) + " ")
            f.write(str(c.getYco()) + " ")
            f.write(str(c.getR()) + "\n")



c = generate_cirkels(300)





write_to_file(c)



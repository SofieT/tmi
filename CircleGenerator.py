from random import random
from Cirkel import Cirkel


def generate_cirkels(amount):

    cirkels = list()

    for a in range(amount):

        cirkels.append(Cirkel(1*random(), 1*random(), 1*random()))



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


<<<<<<< HEAD

c = generate_cirkels(100)
=======
c = generate_cirkels(5)
>>>>>>> 5dadcd9d216892a9d830e5e12502e03c2eb487e6


write_to_file(c)



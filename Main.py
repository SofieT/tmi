#!/usr/bin/python
__author__ = 'Ward Schodts en Robin Goots'

from Cirkel import Cirkel
from Algorithms import Algo1, Algo2, Algo3
from time import time
from CircleGenerator import generate_cirkels


def main():
    algo, aantal_cirkels, lijst = readInput()

    if algo == 1:
        algorithm = Algo1(lijst)
    elif algo == 2:
        algorithm = Algo2(lijst)
    elif algo == 3:
        algorithm = Algo3(lijst)
    else:
        print("Onbekend algoritme.")

    start = time()
    #algorithm.execute()
    end = time()
    #save_output(algorithm.get_intersections(), int((end - start) * 1000), True)
    #save_output_svg(algorithm.circle_list)
    #algorithm_comparison(lijst)

    benchmark_algorithms()

#Deze methode leest het input bestand en verwacht de naam: cirkles.txt

def algorithm_comparison(circle_list):
    algo2 = Algo2(list(circle_list))
    algo3 = Algo3(list(circle_list))

    algo2.execute()
    algo3.execute()

    save_out_comparison_svg(algo2.get_intersections(), algo3.get_intersections(), circle_list, 40)

def readInput():

    lijst = list()
    try:
        with open('input.txt', 'r') as file:
            algo = int(file.readline())
            aantalCirkels = int(file.readline())

            for line in file:
                temp = line.strip().split(' ')
                lijst.append(Cirkel(float(temp[0]), float(temp[1]), float(temp[2])))
    except:
        print('Kan de file "input.txt" niet openen.')

    return algo, aantalCirkels, lijst

def save_output_svg(list):
    with open('circle.svg', 'w') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')

        for l in list:
            f.write('<circle cx="{0}" cy="{1}" r="{2}"/>\n'.format(l.xco, l.yco, l.r))

        f.write('</svg>\n')

def save_out_comparison_svg(intersection1, intersection2, circles, offset):
        with open('circle.svg', 'w') as f:

            f.write('<svg version="1.1" baseProfile="full" viewBox="0 0 {0} {1}" xmlns="http://www.w3.org/2000/svg">\n'.format(offset*2, offset*2))

            for l in circles:
                f.write('<circle cx="{0}" cy="{1}" r="{2}" fill-opacity="0" stroke="black" stroke-width="0.01"/>\n'.format(l.xco + offset, l.yco + offset, l.r))

            for l in intersection1:
                f.write('<circle cx="{0}" cy="{1}" r="{2}" fill="red"/>\n'.format(str(l[0] + offset), str(l[1] + offset), str(0.01 * offset)))

            for l in intersection2:
                f.write('<circle cx="{0}" cy="{1}" r="{2}" fill="yellow"/>\n'.format(str(l[0] + offset), str(l[1] + offset), str(0.01 * offset)))


            f.write('</svg>\n')


def benchmark_algorithms():

    times1 = list()
    times2 = list()
    times3 = list()

    intersections1 = list()
    intersections2 = list()
    intersections3 = list()


    for i in range(20, 251, 20):

        print('Starting for {0} circles'.format(i))

        circles1 = generate_cirkels(i)
        circles2 = list(circles1)
        circles3 = list(circles1)

        algo1 = Algo1(circles1)
        algo2 = Algo2(circles2)
        algo3 = Algo3(circles3)

        start = time()
        algo1.execute()
        end = time()
        times1.append( str(int( (end - start) * 1000 )) )
        intersections1.append(len(algo1.get_intersections()))


        start = time()
        algo2.execute()
        end = time()
        times2.append( str(int( (end - start) * 1000 )) )
        intersections2.append(len(algo2.get_intersections()))

        start = time()
        algo3.execute()
        end = time()
        times3.append( str(int( (end - start) * 1000 )) )
        intersections3.append(len(algo3.get_intersections()))


    with open("times1.txt", "w") as f:
        for i in times1:
            f.write("{0}\n".format(i))

    with open('times2.txt', 'w') as f:
        for i in times2:
            f.write("{0}\n".format(i))

    with open('times3.txt', 'w') as f:
        for i in times3:
            f.write("{0}\n".format(i))


    with open('numberOfIntersections1.txt', 'w') as f:
        for i in intersections1:
            f.write("{0}\n".format(i))

    with open('numberOfIntersections2.txt', 'w') as f:
        for i in intersections2:
            f.write("{0}\n".format(i))

    with open('numberOfIntersections3.txt', 'w') as f:
        for i in intersections3:
            f.write("{0}\n".format(i))







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
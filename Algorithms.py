from BST import Searchtree

__author__ = 'Ward Schodts en Robin Goots'


class Algo1(object):

    cirkel_list = list()
    intersection_list = list()

    def __init__(self, cirkel_list):
        self.cirkel_list = cirkel_list

    def execute(self):
        """
        Voer het algoritme uit.
        """
        while len(self.cirkel_list) != 0:
            # Haal de eerste cirkel van de lijst.
            cirkel = self.cirkel_list.pop(0)

            # Itereer over de andere cirkels en check dat ze overlappen.
            for c in self.cirkel_list:
                if cirkel.check_overlap(c):
                    temp = cirkel.calculate_intersections(c)
                    for t in temp:
                        self.intersection_list.append(t)


    def get_intersections(self):
        """
        Geef de lijst met snijpunten terug.
        """
        return self.intersection_list

class Algo2(object):
    intersection_list = list()

    def __init__(self, circle_list):
        self.circle_list = circle_list

    def execute(self):

        for c in self.circle_list:
            c.twee()

        self.sort_circle_list()
        circle = list()
        while not self.bst.is_empty():
            temp = self.bst.pop()

            if temp.hand == 0:



                for c in circle:
                    if temp.circle.check_overlap(c):
                        intersections = temp.circle.calculate_intersections(c)
                        for t in intersections:
                            self.intersection_list.append(t)
                circle.append(temp.circle)

            else:
                circle.remove(temp.circle)

    def get_intersections(self):
        return self.intersection_list

    def sort_circle_list(self):
        self.bst = Searchtree()
        for c in self.circle_list:
            self.bst.insert(c.linksPunt)
            self.bst.insert(c.rechtsPunt)


class Algo3(object):
    pass
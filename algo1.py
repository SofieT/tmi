__author__ = 'robin'


class algo1(object):

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
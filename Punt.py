__author__ = 'Ward Schodts en Robin Goots'


class Punt():

    def __init__(self, xco, yco, hand = 0, circle = None, partner=None):
        self.xco = xco
        self.yco = yco
        self.hand = hand
        self.partner = partner
        self.circle = circle

    def getXco(self):
        return self.xco

    def getYco(self):
        return self.yco

    def setSegment(self, segment):
        self.segment = segment



    # Methode om twee punten te vergelijken
    # @return true a.s.a. het punt waarop de methode wordt uitgevoerd links ligt van het meegegeven punt
    def compare(self, point):
        """
        jkhgfl
        """
        if self.xco < point.getXco():
            return 0
        if self.xco > point.getXco():
            return 1
        if self.yco < point.getYco():
            return 0
        if self.yco > point.getYco():
            return 1
        if self.hand is None or point.hand is None:
            return 2
        if self.hand < point.hand:
            return 0
        if self.hand > point.hand:
            return 1
        return 4

    def set_partner(self, partner):
        self.partner = partner


    def __str__(self):
        return '(' + str(self.xco) + ' ' + str(self.yco) + ')'

class Box:
    """
        Class for box,checking for correct coordinates

        Attributes:
            a (float): x value of minimum corner (left bottom).
            b (float): y value of minimum corner (left bottom).
            c (float): x value of maximum corner (right top).
            d (float): y value of maximum corner (right top).
            nested(int): How many other boxes contains this box. Default is 0.
            land(bool): True if box is a land. Default is False.

    """

    def __init__(self, a: float, b: float, c: float, d: float, nested=0, land=False):
        """
        The constructor for Box class. Raise ValueError if coordinates are wrong (a > c or b > d)
        Parameters:
            a (float): x value of minimum corner (left bottom).
            b (float): y value of minimum corner (left bottom).
            c (float): x value of maximum corner (right top).
            d (float): y value of maximum corner (right top).
            nested(int): How many other boxes contains this box. Default is 0.
            land(bool): True if box is a land. Default is False.
        """
        self.a, self.b, self.c, self.d, self.nested, self.land = float(a), float(b), float(c), float(d), nested, land
        if (self.a > self.c) or (self.b > self.d):
            raise ValueError('Wrong coordinates')

    def __str__(self):
        """ String representation of Box objects """
        return str(self.a)+" "+str(self.b)+" "+str(self.c)+" "+str(self.d)+" "+"Land: "+str(self.land)+" "+"Nested: "+str(self.nested)

    def overlap(self,box2: object):
        """Check if boxes overlaps.

            Parameters:
            box2 (object) -- Box object

            Returns:
            bool: True if boxes overlaps else False.
        """
        if self.a <= box2.c and self.c >= box2.a and self.d >= box2.b and self.b <= box2.d:
            return True
        else:
            return False

    def contains(self,box2: object):
        """Check if box contains box2.

            Parameters:
            box2 (object) -- Box object to compare

            Returns:
            bool: True if box contains box2 else False.
        """
        if self.a <= box2.a and self.b <= box2.b and self.c >= box2.c and self.d >= box2.d:
            return True
        else:
            return False

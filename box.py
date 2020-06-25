""""Class for box,checking for correct coordinates"""
class Box:
    def __init__(self,a,b,c,d):
        if (a > c) or (b > d):
            raise ValueError('Wrong coordinates')
        else:
            self.a,self.b,self.c,self.d = float(a),float(b),float(c),float(d)

    """Check if boxes overlaps"""
    def check_overlap(self,box2):
        if (self.a <= box2.c and self.c >= box2.a and self.d >= box2.b and self.b <= box2.d):
            return True
        else:
            return False
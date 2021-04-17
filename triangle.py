#!/bin/python
# import functions and consts
from math import sqrt, atan, radians, pi

# Warning!
# Do not fill in all sides of the triangle. The module 
# cannot check the correctness of the sides due to 
# irrationality in the calculation

class Triangle:
    def __init__(self,leg1=None,leg2=None,hyp=None):
        # to build a triangle, you need to know two angles
        if [leg1,leg2,hyp].count(None) > 1:
            raise ArithmeticError("Little information")
        # hypotenus must be more that legs
        if [leg1,leg2,hyp].count(None) == 0:
            if leg1 > hyp or leg2 > hyp:
                raise ArithmeticError("The right triangle isn't build correctly")
        # input val must be int or float or None
        if not isinstance(leg1,(int,float)) and not leg1 is None:
            raise ValueError("Triangle side must be int ot float")
        # if None, we will carculate this side
        elif leg1 == None:
            self.__leg1 = round(sqrt(hyp**2-leg2**2),2)
        else:
            self.__leg1 = float(leg1)
        if not isinstance(leg2,(int,float)) and not leg2 is None:
            raise ValueError("Triangle side must be int or float")
        elif leg2 == None:
            self.__leg2 = round(sqrt(hyp**2-leg1**2),2)
        else:
            self.__leg2 = float(leg2)
        if not isinstance(hyp,(int,float)) and not hyp is None:
            raise ValueError("Triangle side must be int or float")
        elif hyp == None:
            self.__hyp = round(sqrt(leg1**2+leg2**2),2)
        else:
            self.__hyp = float(hyp)
        # there is right angle in right triangle
        self.__a2 = 90.0
        # carculate angle tan(a) = leg1/leg2 => a = atan(leg1/leg2 (without radians)
        self.__a1 = round(atan(self.__leg1/self.__leg2)*180/pi, 2)
        self.__a3 = float(90 - self.__a1)
    
    # print information
    def __repr__(self):
        return f"""sides:
    leg1 = {self.__leg1}
    leg2 = {self.__leg2}
    hypotenuse = {self.__hyp}
angles:
    a1 = {self.__a1}
    a2 = {self.__a2}
    a3 = {self.__a3}"""

    # print full information
    def full(self):
        return f"""sides:
    leg1 = {self.__leg1}
    leg2 = {self.__leg2}
    hypotenuse = {self.__hyp}
angles:
    a1 = {self.__a1}
    a2 = {self.__a2}
    a3 = {self.__a3}
sin:
    sin a = {self.sina}
    sin b = {self.sinb}
cos:
    cos a = {self.cosa}
    cos b = {self.cosb}
tan:
    tan a = {self.tana}
    tan b = {self.tanb}
ctan:
    ctan a = {self.ctana}
    ctan b = {self.ctanb}"""
    
    # carculate triangle size
    @property
    def size(self):
        return (self.__leg1*self.__leg2)/2
    
    # carculate angles sin, cos, etc.
    @property
    def sina(self):
        return self.__leg1/self.__hyp

    @property
    def sinb(self):
        return self.__leg2/self.__hyp

    @property
    def cosa(self):
        return self.sinb

    @property
    def cosb(self):
        return self.sina

    @property
    def tana(self):
        return self.__leg1/self.__leg2

    @property
    def tanb(self):
        return self.__leg2/self.__leg1

    @property
    def ctana(self):
        return self.tanb

    @property
    def ctanb(self):
        return self.tana

# test
if __name__ == "__main__":
    tri = Triangle(3,4)
    print(tri.full())

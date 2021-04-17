#!/bin/python
from math import sqrt, atan, radians, pi

class Triangle:
    def __init__(self,leg1=None,leg2=None,hyp=None):
        if [leg1,leg2,hyp].count(None) > 1:
            raise ArithmeticError("Little information")
        if [leg1,leg2,hyp].count(None) == 0:
            if leg1 > hyp or leg2 > hyp:
                raise ArithmeticError("The right triangle isn't build correctly")
        if leg1 == None:
            self.__leg1 = round(sqrt(hyp**2-leg2**2),2)
        else:
            self.__leg1 = float(leg1)
        if leg2 == None:
            self.__leg2 = round(sqrt(hyp**2-leg1**2),2)
        else:
            self.__leg2 = float(leg2)
        if hyp == None:
            self.__hyp = round(sqrt(leg1**2+leg2**2),2)
        else:
            self.__hyp = float(hyp)
        self.__a2 = 90.0
        self.__a1 = round(atan(self.__leg1/self.__leg2)*180/pi, 2)
        self.__a3 = float(90 - self.__a1)

    def __repr__(self):
        return f"""sides:
leg1 = {self.__leg1}
leg2 = {self.__leg2}                                       hypotenuse = {self.__hyp}                                  angles:                                                    a1 = {self.__a1}
a2 = {self.__a2}                                           a3 = {self.__a3}"""

    @property
    def size(self):
        return (self.__leg1*self.__leg2)/2

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

if __name__ == "__main__":
    tri = Triangle(3,4)
    print(tri)

#!/usr/bin/python3

""" Giorgio Abbadessa - gio.abbadessa@gmail.com """

class IsntVectorError(TypeError):
    pass

class NotSameDegreeError(TypeError):
    pass

class Vector:

    def __init__(self, comp):
        """ pass the components of a vector in a list """
        self.comp = [float(i) for i in comp]

    def __repr__(self):
        """ return repr(self) """
        return "Vector({})".format(self.comp)

    def __str__(self):
        """ return str(self) """
        return "{}".format(self.comp)

    def __len__(self, comp):
        """ return the number of components of the vector """
        return len(self.comp)

    def __getitem__(self, key):
        """ return self.comp[key] """
        return self.comp[key]

    def __setitem__(self, key, value):
        """ set in self[key] a new value """
        self.comp[key] = float(value)

    def __delitem__(self, key):
        """ delete self[key] """
        del(self.comp[key])

    def append(self, value):
        """ append value to vector components """
        self.comp.append(float(value))

    def check(self, value):
        """ return True if value is a vector with same number of
        components else raise some errors"""
        if isinstance(value, Vector):
            if len(self) == len(value): return True
            else: raise NotSameDegreeError(value)
        else: raise IsntVectorError(value)

    def __add__(self, value):
        """ return self + value """
        if self.check(value):
            sum_comp = [self[i]+value[i] for i in range(len(self))]
            return Vector(sum_comp)

    def __neg__(self):
        """ return -self """
        neg_comp = [-i for i in self]
        return Vector(neg_comp)

    def __sub__(self, value):
        """ return self - value """
        return self + (-vector)

    def __abs__(self):
        """ return |self| (magnitude/module of a vector) """
        k = 0
        for i in self: k += i**2
        return k**(.5)

    def __mul__(self, value):
        """ return vector * pure number """
        if type(value) == float or type(value) == int:
            mul_comp = [value*i for i in self]
            return Vector(mul_comp)
        else: raise TypeError(value, "must be a number")

    def scal_mul(self, value):
        """ return self · value """
        if self.check(value):
            scal_mul_comp = [self[i]*value[i] for i in range(len(self))]
            return Vector(scal_mul_comp)

    def vect_mul(self, value):
        """ return self x value (self and value must be 2d)"""
        pass

    def __truediv__(self, value):
        """ return self / value """
        return self * (1 / value)

    def __eq__(self, value):
        """ return self == value """
        if self.check(value):
            if self.comp == value.comp: return True
            else: return False

    def __ne__(self, value):
        """ return self != value """
        return not(self == value)

    def __lt__(self, value):
        """ return self < value """
        if self.check(value):
            if abs(self) < abs(value): return True
            else: return False

    def __gt__(self, value):
        """ return self > value """
        if self.check(value):
            if abs(self) > abs(value): return True
            else: return False

    def __le__(self, value):
        """ return self <= value """
        return ((self < value) or (self == value))

    def __ge__(self, value):
        """ return self >= value """
        return ((self > value) or (self == value))

    def easteregg(self):
        print("you've found the easter egg, LOL")

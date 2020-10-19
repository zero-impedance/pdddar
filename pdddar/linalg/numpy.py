from math import sqrt

import numpy as np

class NpVector:

    def __init__(self, x, y, z, w=1):
        self._arr = np.array([x, y, z, w], dtype=np.float32)

    def __get_x(self):
        return self._arr[0]

    def __set_x(self, x):
        self._arr[0] = x

    x = property(__get_x, __set_x)

    def __get_y(self):
        return self._arr[1]

    def __set_y(self, y):
        self._arr[1] = y

    y = property(__get_y, __set_y)

    def __get_z(self):
        return self._arr[2]

    def __set_z(self, z):
        self._arr[2] = z

    z = property(__get_z, __set_z)

    def __get_w(self):
        return self._arr[3]

    def __set_w(self, w):
        self._arr[3] = w

    w = property(__get_w, __set_w)

    @property
    def rx(self):
        return self.x / self.w

    @property
    def ry(self):
        return self.y / self.w

    @property
    def rz(self):
        return self.z / self.w

    def __iter__(self):
        return iter(self._arr)

    def __repr__(self):
        return "NV({}, {}, {}, {})".format(self.x, self.y, self.z, self.w)

    @property
    def norm(self):
        return sqrt(self.rx ** 2 + self.ry ** 2 + self.rz ** 2)

    def __add__(self, o):
        if self.w != o.w:
            raise ValueError("w doesn't match")
        return NpVector(self.x + o.x, self.y + o.y, self.z + o.z, self.w)

    def __sub__(self, o):
        if self.w != o.w:
            raise ValueError("w doesn't match")
        return NpVector(self.x - o.x, self.y - o.y, self.z - o.z, self.w)

    def __mul__(self, o):
        return NpVector(o * self.x, o * self.y, o * self.z, self.w)

    def __rmul__(self, o):
        return self * o

    def __eq__(self, o):
        return list(self) == list(o)

    def __ne__(self, o):
        return not (self == o)

    def dot(self, o):
        return self.rx * o.rx + self.ry * o.ry + self.rz * o.rz

    def __matmul__(self, o):
        return self.dot(o)

    def cross(self, o):
        if self.w != 1 or o.w != 1:
            raise ValueError("w != 1")

        x = self.y * o.z - self.z * o.y
        y = self.z * o.x - self.x * o.z
        z = self.x * o.y - self.y * o.x
        return NpVector(x, y, z)

    def normalize(self):
        norm = self.norm
        return NpVector(self.x / norm, self.y / norm, self.z / norm, self.w)

__all__ = ["NpVector"]

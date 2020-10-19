from math import sqrt
import unittest

from pdddar.linalg import *

class VectorTestCase(unittest.TestCase):

    def test_props(self):
        v1 = Vector(1, 2, 3, 4)
        self.assertEqual([1, 2, 3, 4], [v1.x, v1.y, v1.z, v1.w])

        v1.x = 5
        v1.y = 6
        v1.z = 7
        v1.w = 8
        self.assertEqual([5, 6, 7, 8], [v1.x, v1.y, v1.z, v1.w])

        v2 = Vector(1, 2, 3)
        self.assertEqual(1, v2.w)

        v3 = Vector(2, 4, 6, 2)
        self.assertEqual([1, 2, 3], [v3.rx, v3.ry, v3.rz])

    def test_norm(self):
        v1 = Vector(1, 2, 3, 4)
        norm = sqrt((1 / 4) ** 2 + (2 / 4) ** 2 + (3 / 4) ** 2)
        self.assertEqual(norm, v1.norm)

    def test_arith(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        v3 = Vector(4, 5, 6, 2)

        v_add = v1 + v2
        self.assertEqual([5, 7, 9, 1], list(v_add))
        self.assertRaises(ValueError, lambda : v1 + v3)

        v_sub = v1 - v2
        self.assertEqual([-3, -3, -3, 1], list(v_sub))
        self.assertRaises(ValueError, lambda : v1 - v3)

        v_mul = v1 * 2
        self.assertEqual([2, 4, 6, 1], list(v_mul))
        self.assertRaises(TypeError, lambda : v1 * object())

        v_rmul = 3.0 * v1
        self.assertEqual([3, 6, 9, 1], list(v_rmul))
        self.assertRaises(TypeError, lambda : object() * v1)

    def test_dot(self):
        v1 = Vector(2, 4, 6, 2)
        v2 = Vector(4, 5, 6)

        self.assertEqual(32, v1 @ v2)
        self.assertEqual(v1.dot(v2), v1 @ v2)

    def test_cross(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        v3 = Vector(4, 6, 8, 2)

        cp = Vector(-3, 6, -3)
        self.assertEqual(cp, v1.cross(v2))
        self.assertRaises(ValueError, v1.cross, v3)
        self.assertRaises(ValueError, v3.cross, v1)

    def test_normalize(self):
        v1 = Vector(1, 2, 3)
        self.assertAlmostEqual(1, v1.normalize().norm, 3)

        v2 = Vector(2, 4, 6, 2)
        self.assertAlmostEqual(1, v2.normalize().norm, 3)

if __name__ == "__main__":
    unittest.main()

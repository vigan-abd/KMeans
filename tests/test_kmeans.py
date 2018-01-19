import unittest
import sys
from os.path import dirname

sys.path.insert(0, dirname(__file__) + '/..')
from libs.algorithms import KMeans


class KMeansTestCase(unittest.TestCase):
    def setUp(self):
        self.alg = KMeans(2, 100, 0.001)
        self.p1 = [1, 2]
        self.p2 = [5, 8]
        self.X = [[1, 2], [1.5, 1.8], [1, 0.6], [5, 8], [8, 8], [9, 11]]
        self.C = [[1.5, 1.8], [8, 8], [7, 7]]

    def test_euclidean(self):
        res = self.alg.euclidean(self.p1, self.p2)
        res = round(res, 2)
        self.assertEqual(res, 7.21)

    def test_manhattan(self):
        res = self.alg.manhattan(self.p1, self.p2)
        self.assertEqual(res, 10)

    def test_squared_euclidean(self):
        res = self.alg.squared_euclidean(self.p1, self.p2)
        self.assertEqual(res, 52)

    def test_chebyshev(self):
        res = self.alg.chebyshev(self.p1, self.p2)
        self.assertEqual(res, 6)

    def test_cluster(self):
        res = self.alg.cluster(self.X, self.C)
        expected = {'pts': [{'p': [1, 2], 'c': 0}, 
            {'p': [1.5, 1.8], 'c': 0}, 
            {'p': [1, 0.6], 'c': 0}, 
            {'p': [5, 8], 'c': 1}, 
            {'p': [8, 8], 'c': 1}, 
            {'p': [9, 11], 'c': 1}], 
            'cts': [[1.1666666666666667, 1.4666666666666666], [7.333333333333333, 9.0]]}
        self.assertAlmostEqual(res, expected, 3)


if __name__ == "__main__":
    unittest.main()

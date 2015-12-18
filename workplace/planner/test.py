import unittest

from route import Route
r = Route()

ab = r.shortestpath('A','B')
ad = r.shortestpath('A','D')
ac = r.shortestpath('A','C')

class TestStringMethods(unittest.TestCase):
    # check minimum distance
    def test_shortest_distance_AB(self):
        self.assertEqual(ab[0], 5)

    def test_shortest_distance_AD(self):
        self.assertEqual(ad[0], 5)

    def test_shortest_distance_AC(self):
        self.assertEqual(ac[0], 9)

    # Check path count
    def test_path_count_AB(self):
        print "A->B"
        r.BFS('A','B')
        self.assertEqual(r.count, 4)

    def test_path_count_CB(self):
        print "C->B"
        r.BFS('C','B')
        self.assertEqual(r.count, 2)

    def test_path_count_AD(self):
        print "A->D"
        r.BFS('A','D')
        self.assertEqual(r.count, 3)

if __name__ == '__main__':
    unittest.main()
import unittest

import canaddress


class TestTagging(unittest.TestCase):
    def test_broadway(self):
        s1 = "1775 Broadway And 57th, Newyork NY"
        canaddress.tag(s1)

#executing test suite
import unittest

class TestCase1(unittest.TestCase):
    def setUp(self):
        print("I am set up method in test case 1")
    def test(self):
        print("I am test case in test case 1")
    def test1(self):
        print("I am another test case in test case 1")
    def tearDown(self):
        print("I am tear Down method in test case 1")

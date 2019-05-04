#python testing
import unittest
class TestDemo(unittest.TestCase):
    def setUp(self):
        print("This is setup method")
    def test(self):
        print("This is test method")
    def test1(self):
        print("This is another test method")
    def tearDown(self):
        print("This is teardown method")
unittest.main()

#python testing
import unittest
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is setup class method")
    def setUp(self):
        print("This is setup method")
    def test(self):
        print("This is test method")
    @classmethod
    def tearDownClass(cls):
        print("This is teardown class method")#order of methods writing doesnt matter
    def test1(self):
        print("This is another test method")
    def tearDown(self):
        print("This is teardown method")
unittest.main()

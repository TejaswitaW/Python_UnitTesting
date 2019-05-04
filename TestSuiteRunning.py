import unittest
from TestCase1 import *
from TestCase2 import *
#you have to load all test from TestCase1
tc1=unittest.TestLoader().loadTestsFromTestCase(TestCase1)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestCase2)

#with tc1 and tc2 we can create testsuite

ts=unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner().run(ts)

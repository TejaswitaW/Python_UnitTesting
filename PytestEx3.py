#implementation of setUpClass and tearDownClass methods
#use of pytest module
import pytest
@pytest.yield_fixture(scope='module')
def setUptearDownClass():
    print("I am set up method")
    yield
    print("I am teardown activity")
def test1(setUptearDownClass):
    print("I am test method 1")
def test2(setUptearDownClass):
    print("I am test method 2")
def test3(setUptearDownClass):
    print("I am test method 3")
def test4(setUptearDownClass):
    print("I am test method 4")

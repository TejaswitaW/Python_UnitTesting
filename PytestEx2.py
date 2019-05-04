#use of pytest module
import pytest
@pytest.yield_fixture()
def setUptearDown():
    print("I am set up method")
    yield
    print("I am teardown activity")
def test1(setUptearDown):
    print("I am test method 1")
def test2(setUptearDown):
    print("I am test method 2")
def test3(setUptearDown):
    print("I am test method 3")
def test4(setUptearDown):
    print("I am test method 4")

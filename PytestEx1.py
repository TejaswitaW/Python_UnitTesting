#use of pytest module
import pytest
@pytest.fixture()
def setUp():
    print("I am set up method")
def test1(setUp):
    print("I am test method 1")
def test2(setUp):
    print("I am test method 2")
def test3(setUp):
    print("I am test method 3")
def test4(setUp):
    print("I am test method 4")

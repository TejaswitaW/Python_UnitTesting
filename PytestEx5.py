#implementation of setUp,tearDown,setUpClass and tearDownClass functionality
import pytest
@pytest.yield_fixture(scope='module')
def setUptearDownClass():
    print("This is class level setup activity")
    yield
    print("This is class level teardown activity")

@pytest.yield_fixture
def setUptearDown():
    print("I am set up method")
    yield
    print("I am tear down activity")
@pytest.mark.run(order=3)
def test1(setUptearDownClass,setUptearDown):
    print("I am test 1")
@pytest.mark.run(order=4)
def test2(setUptearDownClass,setUptearDown):
    print("I am test 2")
@pytest.mark.run(order=2)
def test3(setUptearDownClass,setUptearDown):
    print("I am test 3")
@pytest.mark.run(order=1)
def test4(setUptearDownClass,setUptearDown):
    print("I am test 4")

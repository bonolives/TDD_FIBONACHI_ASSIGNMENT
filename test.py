# Fibonacci assignment : Richard Kwizera and Oliver Balyama
from fibonachi import fibonacci


# defining the test one function for Fibonacci Sequence
def test_one():
    assert fibonacci(3) == [0, 1, 1]

# Adding tests to evolve the Algorithm
def test_two():
    assert fibonacci(5) == [0,1,1,2,3]

def test_three():
    assert fibonacci(4) == [0,1,1,2]

def test_four():
    assert fibonacci(10) == [0,1,1,2,3,5,8,13,21,34]

def test_five():
    assert fibonacci(2) == [0,1]


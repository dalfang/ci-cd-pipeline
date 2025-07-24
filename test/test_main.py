from src.main import add, subtract


def test_add():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(5,5) == 10


def test_subtarct_function():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(10, 5) == 5
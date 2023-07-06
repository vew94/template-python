"""Summary."""
from hoge.math.my_math import add, subtract


def test_add() -> None:
    """Add."""
    assert add(2, 3) == 5


def test_subtract() -> None:
    """Subtract."""
    assert subtract(2, 1) == 1
    assert subtract(5, 5) == 0

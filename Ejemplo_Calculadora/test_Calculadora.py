from Calculadora import suma
import pytest

@pytest.mark.parametrize("a, b, exp", [
    (5, 3, 8),
    (13, -3, 10),
    (-21, -4, -25),
    ])
def test_sumaDosNumerosPositivos(a, b, exp):
    assert suma(a, b) == exp


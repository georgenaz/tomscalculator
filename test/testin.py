import pytest
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent))

from tomscalculator.common import process_calc


def test_calc():
    res = process_calc(1, 10, 'UT')
    assert 10.69 == res.get('result_price')


def test_discounts():
    res = process_calc(1, 1000, 'UT')
    assert 970 == res.get('price_with_discount')

    res = process_calc(1, 5000, 'UT')
    assert 4750 == res.get('price_with_discount')

    res = process_calc(1, 7000, 'UT')
    assert 6510 == res.get('price_with_discount')

    res = process_calc(1, 10000, 'UT')
    assert 9000 == res.get('price_with_discount')

    res = process_calc(1, 15000, 'UT')
    assert 13500 == res.get('price_with_discount')


def test_taxes():
    res = process_calc(10, 10, 'UT')
    assert 106.85 == res.get('result_price')
    assert 6.85 == res.get('state_tax')

    res = process_calc(10, 10, 'NV')
    assert 8 == res.get('state_tax')

    res = process_calc(10, 10, 'TX')
    assert 6.25 == res.get('state_tax')

    res = process_calc(10, 10, 'AL')
    assert 4 == res.get('state_tax')

    res = process_calc(10, 10, 'CA')
    assert 8.25 == res.get('state_tax')

from project import duration, holiday, flights, hotels, estimate
import pytest


def test_duration():
    assert duration("2024-08-13", "2024-08-14") == 1
    assert duration("13 August 2024", "14 August 2024") == 1


def test_holiday(): ...


def test_flight(): ...


def test_hotels(): ...


def test_estimate(): ...

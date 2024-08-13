from project import duration, holiday, flights, hotels, estimate
import pytest


def test_duration():
    assert duration("2024-08-13", "2024-08-14") == 1
    with pytest.raises(SystemExit):
        assert duration("13 August 2024", "14 August 2024")


def test_holiday(): ...


def test_flight(): ...


def test_hotels(): ...


def test_estimate(): ...

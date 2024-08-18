from project import (
    duration,
    holiday,
    flights,
    hotels,
    hotel_estimate,
    flight_estimate,
    package_estimate,
)
import pytest


def test_duration():
    assert duration("2024-08-13", "2024-08-14") == 1
    with pytest.raises(SystemExit):
        assert duration("13 August 2024", "14 August 2024")


def test_holiday():
    assert holiday("Flights") == "Flights"
    assert holiday("Hotels") == "Hotels"
    assert holiday("Both") == "Both"
    assert holiday("Something") == "This is not a valid option"


def test_flight(): ...


def test_hotels():
    assert hotels("Lisboa", "Mid") == "120"
    assert hotels("Tokyo", "High") == "150"
    assert hotels("Barcelona", "Luxury") == None


def test_hotel_estimate(): ...


def test_flight_estimate(): ...


def test_package_estimate(): ...

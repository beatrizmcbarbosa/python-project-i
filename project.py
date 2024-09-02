from datetime import date
import sys
import csv
import requests
import json
import creds

# Destinations available at the travel agency
destinations = {
    "Amsterdam": {"name": "Amsterdam", "IATA": "AMS"},
    "Athens": {"name": "Athens", "IATA": "ATH"},
    "Berlin": {"name": "Berlin", "IATA": "BER"},
    "Bratislava": {"name": "Bratislava", "IATA": "BTS"},
    "Brussels": {"name": "Brussels", "IATA": "BRU"},
    "Bucharest": {"name": "Bucharest", "IATA": "OTP"},
    "Budapest": {"name": "Budapest", "IATA": "BUD"},
    "Copenhagen": {"name": "Copenhagen", "IATA": "CPH"},
    "Dublin": {"name": "Dublin", "IATA": "DUB"},
    "Helsinki": {"name": "Helsinki", "IATA": "HEL"},
    "Lisboa": {"name": "Lisboa", "IATA": "LIS"},
    "Ljubljana": {"name": "Ljubljana", "IATA": "LJU"},
    "Madrid": {"name": "Madrid", "IATA": "MAD"},
    "Nicosia": {"name": "Nicosia", "IATA": "NIC"},
    "Paris": {"name": "PARIS", "IATA": "CDG"},
    "Prague": {"name": "Prague", "IATA": "PRG"},
    "Riga": {"name": "Riga", "IATA": "RIX"},
    "Rome": {"name": "Rome", "IATA": "FCO"},
    "Sofia": {"name": "Sofia", "IATA": "SOF"},
    "Stockholm": {"name": "Stockholm", "IATA": "ARN"},
    "Tallinn": {"name": "Tallinn", "IATA": "TLL"},
    "Malta": {"name": "Malta", "IATA": "MLA"},
    "Vienna": {"name": "Vienna", "IATA": "VIE"},
    "Vilnius": {"name": "Vilnius", "IATA": "VNO"},
    "Warsaw": {"name": "Warsaw", "IATA": "WAW"},
    "Zagreb": {"name": "Zagreb", "IATA": "ZAG"},
}

options = {"Flights", "Hotels", "Both"}


# Missing: typehints
# Missing: docstring


def main():
    tries = 0
    # Display destination options
    print("We offer the following destinations:")
    for i in destinations:
        print("- ", destinations[i]["name"])
    # Prompt user for city choice and exit after 3 tries
    while tries < 3:
        tries += 1
        city_invalid = 0
        try:
            city = input("Where would you like to go? ").strip().capitalize()
            if city in destinations:
                city_code = destinations[city]["IATA"]
                print(f"Thanks for choosing {city}!")
                print(city_code)

                departDate = input(
                    f"When would you like to go?\nPlease answer in the format YYYY-MM-DD: "
                )
                returnDate = input(
                    f"And come back?\nPlease answer in the format YYYY-MM-DD: "
                )
                print(f"{duration(departDate, returnDate)} days")
                # Prompt user for choice of type of holiday
                option = (
                    input(f"What are you looking for today: Flights, Hotels, or Both? ")
                    .strip()
                    .capitalize()
                )
                # If user wants flights, present flights estimate from API
                if option == "Flights":
                    origin = input("Where are you flying from? ").strip().capitalize()
                    print(flights(origin, city_code, departDate, returnDate))
                # If user wants hotels, prompt user for hotel tier and present price
                if option == "Hotels":
                    tier = input("Hotel tier, Low, Mid or High? ").strip().capitalize()
                    print(hotel_estimate(departDate, returnDate, city, tier), "€")
                # If user wants both, present sum of hotels and flights estimates
                if option == "Both":
                    origin = input("Where are you flying from? ").strip().capitalize()
                    tier = input("Hotel tier, Low, Mid or High? ").strip().capitalize()
                    print(
                        package_estimate(departDate, returnDate, city, tier, origin),
                        "€",
                    )
                break
            # If the user has not typed a valid city after 3 tries, exit
            if city not in destinations:
                city_invalid += 1
                if city_invalid == 2:
                    print("That is not a valid city. Please try again")
                    break
        except:
            sys.exit("Invalid input")


def duration(departDate, returnDate):
    # If dates are valid, convert to iso
    try:
        departDate = date.fromisoformat(departDate)
        returnDate = date.fromisoformat(returnDate)

    # If date is not valid, exit
    except:
        sys.exit("Invalid dates")

    return (returnDate - departDate).days


def holiday(option):
    # If user holiday choice is available, return it
    if option in options:
        return option
    else:
        return "This is not a valid option"


def flights(fromEntityId, toEntityId, departDate, returnDate):
    # Retrieve flight prices for origin, destination, and dates

    url = "https://sky-scanner3.p.rapidapi.com/flights/search-multi-city"

    payload = {
        "market": "US",
        "locale": "en-US",
        "currency": "EUR",
        "adults": 1,
        "children": 0,
        "infants": 0,
        "cabinClass": "economy",
        "stops": ["direct", "1stop", "2stops"],
        "flights": [
            {
                "fromEntityId": fromEntityId,
                "toEntityId": toEntityId,
                "departDate": departDate,
            },
            {
                "fromEntityId": toEntityId,
                "toEntityId": fromEntityId,
                "departDate": returnDate,
            },
        ],
    }
    headers = {
        "x-rapidapi-key": f"{creds.api_key}",
        "x-rapidapi-host": "sky-scanner3.p.rapidapi.com",
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        try:
            return response.json()["data"]["filterStats"]["stopPrices"]["direct"][
                "formattedPrice"
            ]
        except KeyError:
            return f"There are no flights for this dates and destination."
    else:
        return f"Error: {response.status_code}, {response.text}"


def hotels(city, tier):
    # Read csv file, find rows with {city} and return the prices
    with open("hotels.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == city:
                if tier == "Low":
                    return row[1]
                if tier == "Mid":
                    return row[2]
                if tier == "High":
                    return row[3]


def hotel_estimate(departDate, returnDate, city, tier):
    # For hotel only, multiply number of days per night cost, based on hotel range selection
    stay = int(duration(departDate, returnDate)) * int(hotels(city, tier))
    return stay


def package_estimate(departDate, returnDate, city, tier, origin):
    # For hotel + flight
    # Get total from flight_estimate and add it to hotel_estimate
    price = 0
    f_price = flights(origin, city, departDate, returnDate)
    h_price = hotel_estimate(departDate, returnDate, city, tier)
    price = f_price + h_price
    return price


if __name__ == "__main__":
    main()

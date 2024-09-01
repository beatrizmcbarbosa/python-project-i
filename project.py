from datetime import date
import sys
import csv
import requests
import json
import creds

# Destinations available at the travel agency
destinations = {
    "Europe": ["Lisboa", "Madrid", "Paris"],
    "Asia": ["Mumbai", "Tokyo"],
    "Oceania": ["Sydney", "Suva"],
    "Africa": ["Nairobi", "Abidjan", "Luanda"],
    "America": ["Lima", "Ciudad do México", "Dallas"],
}

options = {"Flights", "Hotels", "Both"}


# Missing: typehints
# Missing: docstring


def main():
    tries = 0
    # Prompt user for a continent and exit after 3 tries:
    while tries < 3:
        tries += 1
        continent_invalid = 0
        try:
            continent = (
                input("In which continent will your holiday be? ").strip().capitalize()
            )
            # If the continent exists, display cities available in offer
            if continent in destinations:
                city = (
                    input(
                        f"We offer the below options in {continent}:\n{destinations[continent]}\nPlease type the destination where you would like to go: "
                    )
                    .strip()
                    .capitalize()
                )

                # Prompt user to select city option within their continent of choice
                if city in destinations[continent]:
                    departDate = input(
                        f"When would you like to go?\nPlease answer in the format YYYY-MM-DD: "
                    )
                    returnDate = input(
                        f"And come back?\nPlease answer in the format YYYY-MM-DD: "
                    )
                    print(f"{duration(departDate, returnDate)} days")
                    # Prompt user for choice of type of holiday
                    option = (
                        input(
                            f"What are you looking for today: Flights, Hotels, or Both? "
                        )
                        .strip()
                        .capitalize()
                    )
                    # If user wants flights, present flights estimate from API
                    if option == "Flights":
                        origin = input("Where are you flying from? ")
                        print(flights(origin, city, departDate, returnDate))
                    # If user wants hotels, prompt user for hotel tier and present price
                    if option == "Hotels":
                        tier = (
                            input("Hotel tier, Low, Mid or High? ").strip().capitalize()
                        )
                        print(hotel_estimate(departDate, returnDate, city, tier))
                    # If user wants both, present sum of hotels and flights estimates
                    if option == "Both":
                        print(holiday(option))
                    break
                else:
                    print("This city is not part of our offer.")
            # If the user has not typed a valid continent after 3 tries, exit
            if continent not in destinations:
                continent_invalid += 1
                if continent_invalid == 2:
                    print("That is not a valid continent. Please try again")
                    break

        except:
            sys.exit("Invalid input")


def duration(x, y):
    # If dates are valid, convert to iso
    try:
        departDate = date.fromisoformat(x)
        returnDate = date.fromisoformat(y)

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
                "returnDate": returnDate,
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


def hotel_estimate(x, y, city, tier):
    # For hotel only, multiply number of days per night cost, based on hotel range selection
    stay = int(duration(x, y)) * int(hotels(city, tier))
    return f"€{stay:,.2f}"


def flight_estimate(departDate, returnDatee):
    # For flight only
    ...


def package_estimate():
    # For hotel + flight
    # Get total from flight_estimate and add it to hotel_estimate
    ...


if __name__ == "__main__":
    main()

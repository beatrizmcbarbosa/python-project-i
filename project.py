from datetime import date
import sys
import csv

destinations = {
    "Europe": ["Lisboa", "Madrid", "Paris"],
    "Asia": ["Mumbai", "Tokyo"],
    "Oceania": ["Sydney", "Suva"],
    "Africa": ["Nairobi", "Abidjan", "Luanda"],
    "America": ["Lima", "Ciudad do México", "Dallas"],
}

# Missing: typehints
# Missing: docstring


def main():
    tries = 0
    # Prompt user for a continent:
    while tries < 3:
        tries += 1
        continent_invalid = 0
        try:
            continent = (
                input("In which continent will your holiday be? ").strip().capitalize()
            )

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
                    departure = input(
                        f"When would you like to go?\nPlease answer in the format YYYY-MM-DD: "
                    )
                    arrival = input(
                        f"And come back?\nPlease answer in the format YYYY-MM-DD: "
                    )
                    print(f"{duration(departure, arrival)} days")
                    print(hotels(city))
                    break
                else:
                    print("It seems this city is not part of our offer.")

            if continent not in destinations:
                continent_invalid += 1
                # If the user has not typed a valid continent after 3 tries, exit
                if continent_invalid == 2:
                    print("That is not a valid continent. Please try again")
                    break

        except:
            sys.exit("Invalid input")


def duration(x, y):
    # If dates are valid, convert to iso
    try:
        departure_date = date.fromisoformat(x)
        arrival_date = date.fromisoformat(y)

    # If date is not valid, exit
    except:
        sys.exit("Invalid dates")

    return (arrival_date - departure_date).days


def holiday():
    options = {"Flights", "Hotels", "Both"}
    # Prompt user for choice of type of holiday
    option = (
        input(f"What are you looking for today: Flights, Hotels, or Both? ")
        .strip()
        .capitalize()
    )

    if option in options:
        return option
    else:
        print("This is not a valid option")


def flights(): ...


def hotels(city):
    # Read csv file, find rows with {city} and return the prices
    with open("hotels.csv", newline="") as file:
        for row in csv.reader(file):
            if city in row[0]:
                selection = (
                    input(
                        f"Low-range: €{row[1]}\nMid-range: €{row[2]}\nHigh-range: €{row[3]}\nSelect one: "
                    )
                    .strip()
                    .capitalize()
                )
                if selection == "Low-range":
                    return row[1]
                if selection == "Mid-range":
                    return row[2]
                if selection == "High-range":
                    return row[3]
                else:
                    return f"Invalid option."


def hotel_estimate(days):
    # For hotel only
    ...


def flight_estimate(departure, arrival):
    # For flight only
    ...


def package_estimate():
    # For hotel + flight
    # Get total from flight_estimate and add it to hotel_estimate
    ...


if __name__ == "__main__":
    main()

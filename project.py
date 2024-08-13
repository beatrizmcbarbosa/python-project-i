from datetime import date
import sys

destinations = {
    "Europe": ["Lisboa", "Paris", "Madrid"],
    "Asia": ["Mumbai", "Tokyo"],
    "Oceania": ["Sydney", "Suva"],
    "Africa": ["Nairobi", "Abidjan", "Luanda"],
    "America": ["Lima", "Ciudad do México", "Dallas"],
}


def main():
    tries = 0
    # prompt user for a continent:
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

                if city in destinations[continent]:
                    departure = input(
                        f"When would you like to go?\nPlease answer in the format YYYY-MM-DD: "
                    )
                    arrival = input(
                        f"And come back?\nPlease answer in the format YYYY-MM-DD: "
                    )
                    print(duration(departure, arrival))
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
    # Function 2 will, based on city selection, ask the user what they are looking to buy today (Flights, Flight+Hotel, Hotels) and better understand their preferences.
    options = {"Flights", "Hotels", "Both"}
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


def hotels(): ...


def estimate(): ...


if __name__ == "__main__":
    main()

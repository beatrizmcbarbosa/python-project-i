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
    continent = input("In which continent will your holiday be? ").strip().capitalize()

    if continent in destinations:
        city = input(
            f"We offer the below options in {continent}:\n{destinations[continent]}\nPlease type the destination where you would like to go: "
        )
    departure = input(
        f"We are so happy you want to travel to {city}. When would you like to go? Please answer in the format YYYY-MM-DD: "
    )
    arrival = input(f"And come back? Please answer in the format YYYY-MM-DD: ")
    print(duration(departure, arrival))


def duration(x, y):
    # If dates are valid, convert to iso
    try:
        departure_date = date.fromisoformat(x)
        arrival_date = date.fromisoformat(y)

    # If date is not valid, exit
    except:
        sys.exit("Invalid dates")

    return (arrival_date - departure_date).days


def holiday_options(): ...


def flight_search(): ...


def hotels(): ...


def estimate(): ...


if __name__ == "__main__":
    main()

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
        print(
            f"We offer the below options in {continent}:\n{destinations[continent]}\nPlease type the destination where you would like to go"
        )


if __name__ == "__main__":
    main()

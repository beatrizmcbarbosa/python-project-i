# python-project-i
    #### Video Demo:  <URL HERE>
    #### Description: Final project as part of Harvard's CS50 Python Programming
    TODO

<!-- ABOUT THE PROJECT -->
## About the Project
Travel agency

1st Step: Destination

The program will ask the user about their destination. This will present five continent options.

After the user selects their desired continent, they'll be presented with the cities of countries to where the travel agency caters.

2nd Step: Duration
The program will ask the user about the dates when they'd like to travel.

3rd Step: Travel package

The program will ask the user if they would like to see more about Flights, Flight+Hotel, Hotels

If the user is interested in Flights or Flight+Hotel, they will be asked for their departure location

If the user is interested in Flight+Hotel or Hotels, they will be asked for their hotel preferences within (prices displayed are per night): budget (€30 - €70), mid tier (€70 - €200), luxury (€200 - €500)

4th Step: Travel options

The program will then look for real-time flight prices online and look for hotel prices based on tier choice in a csv file.

The program will present the user with the price for the trip based on their choices and describe what is included.

### Execution
The function main will ask the user the questions in Step 1 and then call the other funtions to retrieve the final price and display it to the user

Function 1 will calculate the duration of the trip

Function 2 will, based on city selection, ask the user what they are looking to buy today (Flights, Flight+Hotel, Hotels) and better understand their preferences.

Function 3 will retrieve flight price details, using Skyscanner Flight Search API

Function 4 will retrieve hotel prices from csv file

Function 5 will calculate final cost

### Built With
* [![Python][Python]][Python-url]

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites
### Installation

<!-- USAGE EXAMPLES -->
## Usage

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Image shields](https://shields.io/)
* [README Template](https://github.com/othneildrew/Best-README-Template)

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
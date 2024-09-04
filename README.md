# python-project-i
    #### Video Demo:  <URL HERE>
    #### Description: Final project as part of Harvard's CS50 Python Programming
    TODO

<!-- ABOUT THE PROJECT -->
## About the Project
Travel agency

1st Step: Destination

The program will ask the user about their destination. This will present all capitals of the European Union (EU) as available options.

2nd Step: Duration

The program will ask the user about the dates when they'd like to travel.

3rd Step: Travel package

The program will ask the user if they would like to see more about Flights, Flights+Hotel, Hotels

If the user is interested in Flights or Flights+Hotel, they will be asked for their departure location

If the user is interested in Flight+Hotel or Hotels, they will be asked for their hotel preferences.

4th Step: Travel options

The program will then look for real-time flight prices online and look for hotel prices based on tier choice in a csv file.

The program will present the user with the price for the trip based on their choices and describe what is included.

### Execution
The function main asks the user the questions in Step 1 and then call the other funtions to retrieve the final price and display it to the user.

Function 1 calculates the duration of the trip.

Function 2 checks if the user's holiday option is valid (must be Flights, Hotels or Package).

Function 3 retrieves flight price details, using Rapid API Skyscanner Flight Search API.

Function 4 retrieves hotel prices per night from csv file based on location and tier.

Function 5 calculates hotel total cost.

Note on Function 3: the API key is hidden for this function. It is recommended you get your own API key from Rapid API, which you can get by subscribing to the API "Sky Scanner"

### Built With
* [![Python][Python]][Python-url]

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Img Shields](https://shields.io/)
* [README Template](https://github.com/othneildrew/Best-README-Template)
* [Rapid API](https://rapidapi.com/hub)

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
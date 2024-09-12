# Geolocation Utility

This application will return the details for a location, including the name, latitude and longitude

## Installation

This application is written in Node.JS, so one has to have Node installed.  Subsequently, run `npm install` from the app folder to complete installation.

## Running

There is a .bat file in the bin folder. To run it, execute `geoloc-util.bat <location names>.

Valid scenarios include:
* geoloc-util --locations "Madison, WI"
* geoloc-util "New York, NY" "10001"
* geoloc-util "10001"

## Testing

A set of tests were written in Python, so ensure Python is installed.  Subsequently, run `pip install -r requirements.txt` from the the tests folder to setup tests.

To run tests, execute `pytest` from the root folder.

### _Note:_ the application was written in Node.JS as it has good processing of cmd line arguments. When it came to writing tests, though, Python was chosen as it is better - at the other end - in handling cmd line responses

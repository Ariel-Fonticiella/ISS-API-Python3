# Import the "requests" library & "json" library
import requests

# Set up the parameters we want to pass to the API
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# This is the International Space Station's API that we are connecting to.
# Make a "get" request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)

# Make the same request we did earlier, but with the coordinates of San Fran.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object. Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)

# Headers is a dictionary.
print(response.headers)

# Get the content-type from the dictionary.
print(response.headers["content-type"])

# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# Print the number of people currently in space.
print(data["number"])
print(data)

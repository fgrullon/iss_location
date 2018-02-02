import requests
from geopy.geocoders import Nominatim 

iss = requests.get(url ="http://api.open-notify.org/iss-now.json") #getting coordinates of ISS from API
iss = iss.json()
latitude, longitude = (iss['iss_position']['latitude'], iss['iss_position']['longitude'])

geolocator = Nominatim()

def issCountryLocator(latitude,longitude):
    ll = (str(latitude) +", "+str(longitude))
    location = geolocator.reverse(ll)
    if type(location.address) == str:
         print(location.address)
    else:
       print("The ISS is currently over water")


issCountryLocator(latitude,longitude)

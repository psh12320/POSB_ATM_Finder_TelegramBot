from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="ATMTeleBotFinder")
location = geolocator.geocode("Blk 678/A Woodlands, Singapore")
print(location.latitude)
print(location.longitude)

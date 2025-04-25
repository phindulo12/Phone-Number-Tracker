# pip install folium
# pip install opencage
# pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier
from test import number  # make sure 'number' is like "+27123456789"
import folium
from opencage.geocoder import OpenCageGeocode

# Your OpenCage API Key
key = "yourAPIKEY"
geocoder_api = OpenCageGeocode(key)

# Parse the number
check_number = phonenumbers.parse(number)

# Get the general location (e.g., city or province)
number_location = geocoder.description_for_number(check_number, "en")
print(f"Detected region: {number_location}")

# Get the service provider (e.g., MTN, Vodacom)
service_provider = carrier.name_for_number(check_number, "en")
print(f"Carrier: {service_provider}")

# Query OpenCage for geocoding the location name (broad area)
results = geocoder_api.geocode(number_location)

if results and len(results):
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Coordinates: {lat}, {lng}")

    # Generate a map with folium
    map_location = folium.Map(location=[lat, lng], zoom_start=10)
    folium.Marker([lat, lng], popup=number_location).add_to(map_location)
    map_location.save("mylocation.html")
    print("Map saved as mylocation.html")
else:
    print("Could not geocode the location from the number.")





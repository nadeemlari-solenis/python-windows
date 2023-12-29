import phonenumbers
from myphone import number
from phonenumbers import geocoder, carrier
phone = phonenumbers.parse(number)
country_location = geocoder.description_for_number(phone,"en")
print(country_location)
provider = carrier.name_for_number(phone,"en")
print(provider)
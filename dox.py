
import os

name = input("Target's Full Name: ")

usr = input("Target's Usernames: ")

country = input("Target's Country: ")

region = input("Target's Region OR State: ")

address = input("Target's Home Address: ")

ip = input("Target's IP: ")

addip = input("Additional ip info: ")

city = input("Target's City: ")

pn = input("Target's Phone Number: ")

email = input("Target's Email: ")

lat = input("Coordinates, Latitude: ")

lon = input("Coordinates, Longitude: ")

isp = input("Targets Internet Service Provider: ")

zip = input("Target's Zip Code: )

yn = input("who to credit the dox to: ")

print(f"""
___  __   __                      __   ___     __         ___       ___ 
 |  /  \ /  \ |        |\/|  /\  |  \ |__     |__) \ /     |  |__| |__  
 |  \__/ \__/ |___     |  | /~~\ |__/ |___    |__)  |      |  |  | |___ 

=====================================================================================
                _   _ _____         _        _____            _ _ _   _             
     /\         | | (_)  __ \       | |      / ____|          | (_) | (_)            
    /  \   _ __ | |_ _| |__) |__  __| | ___ | |     ___   __ _| |_| |_ _  ___  _ __  
   / /\ \ | '_ \| __| |  ___/ _ \/ _` |/ _ \| |    / _ \ / _` | | | __| |/ _ \| '_ \ 
  / ____ \| | | | |_| | |  |  __/ (_| | (_) | |___| (_) | (_| | | | |_| | (_) | | | |
 /_/    \_\_| |_|\__|_|_|   \___|\__,_|\___/ \_____\___/ \__,_|_|_|\__|_|\___/|_| |_|

=====================================================================================
""")

print("\u001b[31m[#]Name: \u001b[0m " +      name)
print("\u001b[31m[#]Usernames:  \u001b[0m" + usr)
print("\u001b[31m[#]Country: \u001b[0m: " +   country)
print("\u001b[31m[#]Region Or State: \u001b[0m" +    region)
print("\u001b[31m[#]City: \u001b[0m" + city)
print("\u001b[31m[#]Address: \u001b[0m" +   address)
print("\u001b[31m[#]Zip Code: \u001b[0m" +   zip)            
print("\u001b[31m[#]Internet Service Provider: \u001b[0m" +   isp)
print("\u001b[31m[#]Zip Code: \u001b[0m" + zip)
print("\u001b[31m[#]Latitude: \u001b[0m" + lat)
print("\u001b[31m[#]Longitude: \u001b[0m" + lon)
print("\u001b[31m[#]IP: \u001b[0m" + ip)
print("\u001b[31m[#]Additional IP info: \u001b[0m" + addip)
print("\u001b[31m[#]Phone Number: \u001b[0m" + pn)
print("\u001b[31m[#]Email: \u001b[0m" + email)
print("\u001b[31m[#]DOXXED BY: \u001b[0m" + yn)

import os
import socket

import urllib3.exceptions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent="ATMTeleBotFinder")

from fake_useragent import UserAgent

# Chrome Options to get through CAPTCHA and enter login details to enter booking site.
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--enable-javascript")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
ua = UserAgent()
userAgent = ua.random
print("User Agent is:", userAgent)
chrome_options.add_argument(f'user-agent={userAgent}')
# Use the `install()` method to set `executabe_path` in a new `Service` instance:
service = Service(executable_path=ChromeDriverManager().install())
os.chmod('C:/Users/Shricharan/Downloads/chromedriver_win32 (1)/chromedriver.exe', 755)
# Pass in the `Service` instance with the `service` keyword:
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get("https://banksinsingapore.net/dbs-atm-near-me/")
print("Entered website already")
driver.implicitly_wait(2)
print("Chrome Browser Initialized in Headless Mode")
threecharstring = ''
locationslist = []
threecharstringlist = []
latlonglist = []
errorlocations = []
locnlatlong = []
for number in range(6, 885):
    try:
        text = driver.find_element(By.XPATH, f'//*[@id="post-60"]/div/div/p[{number}]').text
# first atm location xpath: //*[@id="post-60"]/div/div/p[6]/text()[1]
# last atm location xpath: //*[@id="post-60"]/div/div/p[884]/text()[1]
        try:
            locationlist = text.splitlines()[1]
            print(locationlist)
            locations = locationlist.split(' ')
            threecharstring = ' '.join(locations[1:4])
            locationslist += [' '.join(locations[1:])]
            print(threecharstring)
            threecharstringlist += [threecharstring]
            geolocatorthree = threecharstring + ',' + ' ' + 'Singapore'
            print(geolocatorthree)
            atmlocation = geolocator.geocode(geolocatorthree)
            latlong = (atmlocation.latitude, atmlocation.longitude)
            latlonglist += latlong
            print(latlong)
            locnlatlong += (threecharstring, atmlocation.latitude, atmlocation.longitude)
        except AttributeError:
            errorlocations += [threecharstring]
            locationslist.remove(locationslist[-1])
            threecharstringlist.remove(threecharstringlist[-1])
            continue
    except socket.error:
        print("CAUGHT SOCKET TIMEOUT ERROR.")
        continue


print(locationslist)
print(threecharstringlist)
print(latlonglist)
print(errorlocations)
print(locnlatlong)
driver.quit()

f = open("atmlocsafterchange.txt", "a")
f.write("Locations list is: ")
f.write(str(locationslist))
f.write("\n")
f.write("Threecharstring List is: ")
f.write(str(threecharstringlist))
f.write("\n")
f.write("Lat/Long List is: ")
f.write(str(latlonglist))
f.write("\n")
f.write("Error Locations are: ")
f.write(str(errorlocations))
f.write("\n")
f.write("Locations n LatLongs are: ")
f.write(str(locnlatlong))
f.close()

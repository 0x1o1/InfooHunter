# Author: Fawaz Al-Hulays - 0x1o1
# To run the script in "Windows cmd" for example : py -3 infoscript.py "google.com"   or   python3 infoscript.py "google.com"
# To use this script in the right way , you need to install the following libraries:( sys , requests , socket , json , pyfiglet )

# We will be using "sys library" To use command line arguments.
import sys

# Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs,
# or to form-encode your PUT & POST data — but nowadays, just use the json method!
import requests

# Socket library i use it to i deal with server and client communication Using (TCP - UDP) protocols & we use it to get some details about the HOST.
import socket

# Json module is used for handling JSON Data, i use it here because its easier and more readable than pick ling/unpickling a dictionary.
import json 

# pyfiglet is a full port of FIGlet (http://www.figlet.org/) into pure python.
# It takes ASCII text and renders it in ASCII art fonts (like the title above, which is the 'block' font).
from pyfiglet import  Figlet

# To import the text that i want to see it as font or style in my script when i run it.
import Logo
Logo.Logo.run(path="InfooHunter")

# To check the domain
if len(sys.argv) < 2 :
    print ("Usage : " + sys.argv[0] + "<url>")
    sys.exit(1)
# Get URL from Command Line Argument
req = requests.get("https://" + sys.argv[1])

# here we can get the banner header
print("\n"+str(req.headers))

# here we get the host name using  gethostbyname() function from the socket module.
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is :" + gethostby_ + "\n")

#ipinfo.io
# Here we use json  method to parse the response from ipinfo API because it returns JSON data.
# We can get  information about an IP address, such as location, ASN details, and more.
req_two = requests.get("https://ipinfo.io/" + gethostby_ + "/json") 
resp_ = json.loads(req_two.text)

# To print "Location" of the terget
print("Location : " + resp_["loc"])

# To print "Region" of the terget
print("Region: " + resp_["region"])

# To print "City" of the terget
print("City: "+resp_["city"])

# To print "Country" of the terget
print("Country: " + resp_["country"])
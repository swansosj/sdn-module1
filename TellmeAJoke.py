"""

This is a simple Python Script that returns a joke via an API when ran
    Python Syntax Speaking this is the Banner of my code. Which
      is ignored by Python and for documenation purposes only
"""


#This is a comment
#Python ignores any comment and they are strictly for making notes
#They are all annotated starting with a # symbol

#This imports the requests library
import requests

#This defines a variable called URL and it's value is a text string of the API site we are interested in
URL = "https://api.icndb.com/jokes/random"

#This defines an empty dictionary not a list annoted with the curly braces {} but it is empty or has no values
payload = {}

#This also defines a dictionary with {} and does have a value.  Dictionaries are key value pairs and formatted such as below
#This dictionary has a key of Accept and a Value of application-json which will be included in our headers
headers = {'Accept': 'application/json'}


#Creates a variable called response and the value is the result of a HTTP GET request from our URL, with our specified headers
#And store any data in our empty payload dictionary.  We aren't done just yet!
response = requests.get(URL, headers=headers, data=payload)

#Creates a variable called responseJSON and the value is our response variable converted to JSON format
responseJSON = response.json()

#prints our responseJSON variable
print(responseJSON)

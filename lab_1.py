# https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
import urllib.request
contents = urllib.request.urlopen("http://www.google.com/").read() 
print(contents)
print("")

contents = urllib.request.urlopen("https://raw.githubusercontent.com/Malcolm1998/CMPUT404Lab1/master/lab_1.py").read() 
print(contents)
print("")

import requests
print("requests version: "+requests.__version__+"\n")

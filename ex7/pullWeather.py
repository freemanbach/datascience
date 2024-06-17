#!/bin/env python
# author : flo@radford.edu
# date   : 2024.06.16
# ver    : 0.0.1
# desc   : getting 5 dates data for certain city in the US
# API    : https://openweathermap.org/forecast5 

import requests
import json

def main():
    # Enter in your APi Key along with the long and lat coordiates of your city of choice
    apikey=""
    #a = requests.get("https://api.openweathermap.org/data/2.5/weather?q=san diego,ca,us&units=imperial&appid="+apikey)
    a = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=5.5602&lon=-0.1576&units=imperial&appid="+apikey)
    print(a.text)

if __name__ == "__main__":
    main()

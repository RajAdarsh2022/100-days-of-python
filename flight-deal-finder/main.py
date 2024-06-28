#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
import dotenv
import os
import datetime

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData


data_manager = DataManager()
flight_search = FlightSearch()




dotenv.load_dotenv()

def create_target_locations_list():

    sheet_data = data_manager.fetch_data()
    target_locations = sheet_data['prices']
    target_location_list = []
    for location in target_locations:
        city = location['city']
        city_iata_code = location['iataCode']
        allowable_price = location['lowestPrice']

        location_data = FlightData('LON', city_iata_code, 1, allowable_price)
        target_location_list.append(location_data)
    return target_location_list


target_location = create_target_locations_list()
start = input("Enter the search start date(in yyyy-mm-dd) :")
end = input("Enter the search start date(in yyyy-mm-dd) :")

start_list = start.split('-')
start_date = datetime.datetime(int(start_list[0]), int(start_list[1]), int(start_list[2]))
print(type(start_date))
print(start_date)












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

def find_minimum_fare_over_duration(location , start_date, end_date):

        current_date = start_date
        fare_prices_list = []
        while current_date <= end_date:

            fare_prices_list.append(flight_search.get_minimum_fare(location, current_date.strftime("%Y-%m-%d")))
            current_date += datetime.timedelta(days=1)
        print(fare_prices_list)
        # minimum_fare_price = min(fare_prices_list)
        # print(f"Minimum price fare for {location.origin_location_code} to {location.destination_location_code} is : {minimum_fare_price}")


target_location = create_target_locations_list()

start = input("Enter the search start date(in yyyy-mm-dd) :")
end = input("Enter the search start date(in yyyy-mm-dd) :")
start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
end_date = datetime.datetime.strptime(end, "%Y-%m-%d")


for location in target_location:
    print(f"For {location.origin_location_code} to {location.destination_location_code}")
    find_minimum_fare_over_duration(location, start_date, end_date)














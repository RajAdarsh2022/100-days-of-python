#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
import dotenv
import os

from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
flight_search = FlightSearch()



dotenv.load_dotenv()

amadeus_api_key = os.getenv('AMADEUS_API_KEY')
amadeus_api_secret = os.getenv('AMADEUS_API_SECRET')
amadeus_iata_code_access_token = os.getenv('AMADEUS_IATA_CODE_ACCESS_TOKEN')

iata_code_access_base_url = os.getenv('IATA_CODE_ACCESS_BASE_URL')


json_data = data_manager.fetch_data()
row_list = json_data['prices']
for row in row_list:
    print(row)
    city_name = row['city']
    lowest_price = row['lowestPrice']
    id = row['id']

    #getting the IATA code from Amadeus city-search API
    url = f"{iata_code_access_base_url}?keyword={city_name.upper()}"
    header = {
        "Authorization" : f"Bearer {amadeus_iata_code_access_token}"
    }
    iata_response = requests.get(url=url, headers=header)
    iata_response.raise_for_status()
    iata_response_json = iata_response.json()
    iata_code = iata_response_json['data'][0]['iataCode']
    print(iata_code)


    json_payload = {
        'price' :  {
            'city' : city_name,
            'iataCode' : iata_code,
            'lowestPrice' : lowest_price,
        }
    }
    data_manager.update_data(id, json_payload)





import requests
import dotenv
import os

dotenv.load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.api_key = os.getenv('AMADEUS_API_KEY')
        self.api_secret = os.getenv('AMADEUS_API_SECRET')
        self.api_access_token = self.get_new_token()
        self.base_url = os.getenv('FLIGHT_SEARCH_BASE_URL')
    

    def get_new_token(self) -> str:
        """Generates new token for authentication"""

        token_generation_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=token_generation_endpoint, headers=header, data=body)
        response.raise_for_status()
        response_data = response.json()
        return response_data['access_token']
    
    
    def get_journey_data(self, journey, journey_date):
        """Retrives the journey data for a journey on a particular date"""

        origin_code = journey.origin_location_code
        destination_code = journey.destination_location_code
        adult_count = journey.num_of_adults
        allowable_price = journey.allowable_price

        
        api_endpoint = f"https://{self.base_url}/shopping/flight-offers"
        header = {
            'authorization' : f"Bearer {self.api_access_token}"
        }

        request_body = {
            'originLocationCode' : origin_code,
            'destinationLocationCode' : destination_code,
            'departureDate' : journey_date,
            'adults' : adult_count
        }

        response = requests.get(url=api_endpoint, params=request_body, headers=header)
        response.raise_for_status()
        return response.json()
        # first_price = response_data['data'][0]['price']['grandTotal']
        # print(type(first_price))

    def get_minimum_fare(self, journey, journey_date):
        """Retrives the minimum fare for a particular journey on a given date"""
        data = self.get_journey_data(journey, journey_date)
        fare_data = data['data']
        fare_price = []
        for fare in fare_data:
            fare_price.append(float(fare['price']['grandTotal']))
        
        minimum_fare = min(fare_price)
        print(f"Minimum fare from {journey.origin_location_code} to {journey.destination_location_code} is : {minimum_fare}")
        



    

    

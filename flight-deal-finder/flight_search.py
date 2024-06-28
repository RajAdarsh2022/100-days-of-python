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
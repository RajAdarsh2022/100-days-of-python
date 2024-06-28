import requests
import dotenv
import os

dotenv.load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = os.getenv('SHEET_ENDPOINT')
    
    def fetch_data(self) -> dict:
        """Fetches the data from the sheets"""
        response = requests.get(url=self.endpoint)
        response.raise_for_status()
        response_data = response.json()
        return response_data
    
    def add_data(self, data_to_be_added : dict) -> bool:
        """Adds the data to the sheet"""
        response = requests.post(url=self.endpoint , json=data_to_be_added)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def update_data(self, row_no : int, new_data : dict) -> bool:
        """Updates the row data on the mentioned row_no with new_data"""
        update_endpoint = self.endpoint + f"/{row_no}"
        response = requests.put(url= update_endpoint, json= new_data)
        if response.status_code == 200:
            return True
        else:
            return False


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, origin : str, destination: str, adults : int, allowable_price : int):
        self.origin_location_code = origin
        self.destination_location_code = destination
        self.num_of_adults = adults
        self.allowable_price = allowable_price
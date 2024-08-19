
class FlightData:
    def __init__(self):
        self.low_price_found: bool = False
        self.cheapest_flight: dict = {}

    def find_lowest_price(self, flight_data, lowest_price, city_name):
        print(f"Checking prices for {city_name}")
        print(lowest_price)
        for flight in flight_data:
            if float(flight["price"]["total"]) < lowest_price:
                print(f"Found a cheap price to {city_name} for {flight["price"]["total"]}")
                self.cheapest_flight = flight
                self.low_price_found = True
            else:
                print(f"No cheap flights found for {city_name}")






class Flight:
    def __init__(self, flight_number: str, destination: str, seats_available: int, base_price: float):
        self.flight_number = flight_number
        self.destination = destination
        self.seats = seats_available
        self.base_price = base_price

    def book_ticket(self, passenger_name: str):
        if self.seats == 0:
            print(f"Dear {passenger_name}, there are no seats available.")
        else:
            self.seats -= 1
            print(f"Dear {passenger_name}, your seat has been booked.")

    def ticket_price(self):
        return self.base_price + 100
    
    def disp_flight_info(self):
        print(f"Flight Number: {self.flight_number}, Destination: {self.destination}, Seats: {self.seats}, Ticket price: {self.ticket_price()}")


class DomesticFlight(Flight):
    def ticket_price(self):
        return self.base_price * 21 / 20
    

class InternationalFlight(Flight):
    def ticket_price(self):
        return self.base_price * 13 / 10


class Passenger:
    def __init__(self, name: str, passport_number: str):
        self.name = name; self.passport_num = passport_number
    
    def book_flight(self, flight: Flight):
        flight.book_ticket(self.name)



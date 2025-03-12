from datetime import *
from random import randint

# travel planner
nights = int(input("Enter how many night you want to stay: "))

hotel_cost = nights * 140

cities_and_cost = {"Charlotte": 183, 'tampa': 220, 'Pittsburgh': 222, 'Los angeles': 475}

while True:
    city = input("Enter the city you want to visit: ")

    if city not in cities_and_cost.keys():
        print("Invalid destination.")
    else:
        flight_ticket_cost = cities_and_cost[city]
        break

days = int(input("Enter number of days for car rent: "))

car_rental_cost = days * 40

if days >= 7:
    car_rental_cost -= 50
elif days >= 3:
    car_rental_cost -= 20

total = hotel_cost + flight_ticket_cost + car_rental_cost

print(f"Hotel cost: {hotel_cost}")
print(f"Flight Ticket Cost: {flight_ticket_cost}")
print(f"Car Rental Cost: {car_rental_cost}")
print(f"Total cost: {total}")


# random date suggestion
def generate_random_date(start_date: str, end_date: str):
    if start_date.count("/") != 2 or 2 != end_date.count("/"):
        print("Invalid format")
    elif start_date[2] != '/' or end_date[2] != '/' or start_date[5] != '/' or end_date[5] != '/':
        print("Invalid format.")
    elif len(start_date[6:]) != 4 or len(end_date[6:]) != 4:
        print("Invaid format.")
    else:
        sd_month = int(start_date[:2])
        sd_date = int(start_date[3:5])
        sd_year = int(start_date[6:])
        ed_month = int(end_date[:2])
        ed_date = int(end_date[3:5])
        ed_year = int(end_date[6:])
        sd_datetime_obj = datetime(sd_year, sd_month, sd_date)
        ed_datetime_obj = datetime(ed_year, ed_month, ed_date)
        diff = ed_datetime_obj - sd_datetime_obj
        if diff.days <= 0:
            print("Invalid date.")
        else:
            random_days = randint(0, diff.days)
            # this doesent work fully. i have tried my best.
            new_date = datetime(random_days // 365, (random_days % 365) // 12, ((random_days % 365) % 12) // 24) + diff
            print(new_date)

generate_random_date("12/31/2025", "12/31/2026")
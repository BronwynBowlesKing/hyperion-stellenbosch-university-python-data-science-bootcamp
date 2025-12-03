"""Write functions to calculate a user’s total holiday cost"""

# Define the needed functions
def hotel_cost(num_nights, pppn = 1100):
    hotel_total = num_nights * pppn
    return hotel_total

def plane_cost(city_flight):
    if city_flight == 1:
        flight = 4000
    elif city_flight == 2:
        flight = 3000
    elif city_flight == 3:
        flight = 2500
    else:
        print("Press 1 for Cape Town flights, 2 for Durban flights, or 3 for Johannesburg flights.")  
    return flight

def car_rental(rental_days, rental_pd = 900):
    rental = rental_days * rental_pd
    return rental

def holiday_cost(hotel_total, flight, rental):
    grand_total = hotel_total + flight + rental
    return grand_total

# Request user's input
city_flight = input("Press 1 for Cape Town flights, 2 for Durban flights, or 3 for Johannesburg flights.") 
num_nights = int(input("How many nights will you be staying in your chosen city?"))
rental_days = input("How many days do you need to rent a car?")

# Use the functions defined with user input
hotel_total = hotel_cost(num_nights)
flight = plane_cost(int(city_flight))
rental = car_rental(int(rental_days))
grand_total = holiday_cost(hotel_total, flight, rental)

# Provide costs to the user
print(f"Your accomodation is booked as follows:\n Cost of your hotel: R{hotel_total}. \n Cost of your flight: R{flight} return. \n Cost of your car rental: R{rental}. \n Grand total cost: R{grand_total}.")
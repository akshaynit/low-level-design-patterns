'''
This code demostrates an example of strategy pattern.
The strategy here is how do we get best riders for a customer in a ride booking app
'''

from abc import ABC, abstractmethod
import math

'''
Person class represents a person.
'''
class Person:

     def __init__(self, name, location_x_coord, location_y_coord):
        self.name = name
        self.location_x_coord = location_x_coord
        self.location_y_coord = location_y_coord
        self.rating = 0

'''
Rider class represents a rider.
'''
class Rider(Person):

    def __init__(self, name, location_x_coord, location_y_coord):
        super().__init__(name, location_x_coord, location_y_coord)

'''
Customer class represents a customer who requests rides.
'''
class Customer(Person):

    def __init__(self, name, location_x_coord, location_y_coord):
        super().__init__(name, location_x_coord, location_y_coord)

'''
Abstract class that represents a strategy.
'''
class RideMatchingStrategy(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def find_matching_riders(self):
        pass

'''
Concrete class that represents a strategy where nearest riders are given priority.
'''
class NearestRidersFirst(RideMatchingStrategy):

    def __init__(self):
        pass

    def calc_distance(self, rider, customer):
        rider_x, rider_y = rider.location_x_coord, rider.location_y_coord
        customer_x, customer_y = customer.location_x_coord, customer.location_y_coord

        return math.sqrt((rider_x - customer_x) ** 2 + (rider_y - customer_y) ** 2)

    def find_matching_riders(self, riders, customer):
        riders.sort(key = lambda x: self.calc_distance(x, customer))
        return riders

'''
Concrete class that represents a strategy where highest rated riders are given priority.
'''
class HighestRatingRidersFirst(RideMatchingStrategy):

    def __init__(self):
        pass

    def find_matching_riders(self, riders, customer):
        riders.sort(key = lambda x: -x.rating)
        return riders
    
def get_strategy(strategy_name):

    if strategy_name == "highest_rating":
        return HighestRatingRidersFirst()
    elif strategy_name == "nearest_distance":
        return NearestRidersFirst()

'''
Main code to simulate a customer requesting ride and riders getting prioritized based on different strategies
'''
def match_riders():

    # creating customer and rider objects
    customer = Customer("customer_a", 0, 0)
    rider_a = Rider("rider_a", 5, 5)
    rider_b = Rider("rider_b", 3, 3)
    rider_c = Rider("rider_c", 0.5, 0.5)

    # providing random ratings to riders
    rider_a.rating = 4.7
    rider_b.rating = 4.8
    rider_c.rating = 3
    riders = [rider_a, rider_b, rider_c]

    # simulating strategy where higher rating riders are matched first, the result is just the list of riders sorted by their rating
    high_rating_strategy = get_strategy("highest_rating")
    riders = high_rating_strategy.find_matching_riders(riders, customer)
    print(" ".join(x.name for x in riders))

    # simulating strategy where higher rating riders are matched first, the result is just the list of riders sorted by their distance
    # from the customer
    nearest_distance_strategy = get_strategy("nearest_distance")
    riders = nearest_distance_strategy.find_matching_riders(riders, customer)
    print(" ".join(x.name for x in riders))

# calling main code
match_riders()

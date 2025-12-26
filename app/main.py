class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
    
    def serve_cars(self, list_of_cars: list):
        cash_received = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                income = self.calculate_washing_price(car)
                self.wash_single_car()
                cash_received += income
        return cash_received
        
    
    def calculate_washing_price(self, car):
        differences_value = (self.clean_power - car.clean_mark)
        return round((car.comfort_class * differences_value * self.average_rating) / self.distance_from_city_center, 1)

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power
    
    def rate_service(self, new_rating):
        self.average_rating = round((self.average_rating * self.count_of_ratings + new_rating) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
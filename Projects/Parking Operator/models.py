from datetime import datetime

class Car:
    __index__ = 1 
    def __init__(self, num_plate) -> None:

        self.id = self.__index__
        self.registered_at = datetime.now()
        self.paid = False
        self.num_plate = num_plate
        self.price = float() # price depending on the duration of stay in minutes
        self.exited_at = None

        Car.__index__ += 1


    def display_info(self): 
        total_seconds = (datetime.now() - self.registered_at).total_seconds()
        price = float() if total_seconds <= 60 else (total_seconds / 60) * 0.50 
        self.price = round(price, 2) if not self.paid else self.price
        print(f"|  {self.id}  |   {self.num_plate}  | {self.registered_at.strftime('%H:%M %m-%d-%Y')} |  {self.paid} |" \
        f" $ {self.price} | {self.exited_at.strftime('%H:%M %m-%d-%Y') if self.exited_at != None else 'N/A'} |")


class CarPark: 

    def __init__(self, name, max_car) -> None: 
        self.max_car = max_car
        self.name = name
        self.car_collection  = []
        self.history = []


    def __str__(self) -> str:
        return self.name


    def get_car(self, car_id): 

        for car in self.car_collection:

            if car.id == car_id: 

                return car 
    def add_to_car_collection(self, car:Car): 
        
        if self.car_collection.__len__() >= self.max_car: 
            return 

        self.car_collection.append(car)


    def display_car_collection(self): 

        if self.is_carpark_empty(): 
            return 
        
        print("|  ID | Number Plate|     Entry Time   |  Paid  | Price | Exit Time |")
        for car in self.car_collection:
            
            car.display_info()
            

    def is_carpark_empty(self) -> bool:


        return True if self.car_collection.__len__() <= 0 else False

    def is_full(self) -> bool: 

        return True if self.car_collection.__len__() >= self.max_car else False



    def remove_car(self, car_instance): 

        new_collection = []

        for car in self.car_collection:
        
            if car.id != car_instance.id: 

                new_collection.append(car)
                
        
        self.car_collection = new_collection





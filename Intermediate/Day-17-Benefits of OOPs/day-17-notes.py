class User:
    def __init__(self ,id,name):
        print("New user being created")
        self.id = id
        self.name = name
        self.followers = 0

user_1 = User('001','sreehari')
user_2 = User('002','sreerag')
print(user_1.followers)


class Car:
    def __init__(self,seats):
        self.seats = seats
        
my_car = Car(5)
print(my_car.seats)
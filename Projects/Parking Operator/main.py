from models import CarPark, Car
from helpers import clear_display
from datetime import datetime

mycarpark = CarPark("MyCarpark", 5)

choice = ''

while choice != '9': 
    
    print(f"\nWelcome to {mycarpark.name}! Please pick a task below: ")
    print("\n1. Display all cars.")
    print("2. Add a car.")
    print("3. Pay for parking.")
    print("4. Remove car.")
    print("5. Display history")
    print("9. Quit program.")

    
    choice = input("\nPlease pick a task above: ")

    if choice == '1': 
        clear_display()
        if mycarpark.is_carpark_empty(): 
            print(f"\nWarning: {mycarpark.name} is empty!")
            continue


        mycarpark.display_car_collection()

    elif choice == '2':

        if mycarpark.is_full(): 
            
            clear_display()
            print(f"\nWarning: {mycarpark} is at max capacity!")
            continue

        num_plate_in = input("\nPlease enter the number plate: ")

        mycarpark.add_to_car_collection(Car(num_plate_in))

        clear_display()

        mycarpark.display_car_collection()

    elif choice == '3': 
        
        clear_display()
        if mycarpark.is_carpark_empty(): 
            
            print(f"\nWarning: {mycarpark} park is empty!")

            continue

        mycarpark.display_car_collection()
        print("\nNote: Type 0 to cancel")
        
        car_id = int(input("\nPlease select a car id: "))

        if car_id == 0: 
            clear_display()
            continue

        new_collection = []

        for car in mycarpark.car_collection:
            
            if car.id == car_id:

                if car.paid: 
                    clear_display()
                    print(f"\nWarning: customer already paid for this parking.")
                    
                    continue

                amount_paid = float(input(f"Cost for car with the number plate [{car.num_plate}] is $ {car.price}: "))

                if amount_paid != car.price:
                    clear_display()
                    print(f"\nWarning: Payment amount did not match!")
                    continue
                car.paid = True
                car.price = amount_paid
                new_collection.append(car)
                clear_display()
                continue

            new_collection.append(car)
        
        
        mycarpark.car_collection = new_collection

        

        mycarpark.display_car_collection()


    elif choice == '4': 
        clear_display()

        mycarpark.display_car_collection()

        print("\nNote: Type 0 to cancel")
        
        car_id = int(input("\nPlease select a car id: "))

        if car_id == 0: 
            clear_display()
            continue

        car = mycarpark.get_car(car_id)

        if not car.paid: 
            clear_display()
            print("\nWarning: customer has not paid!")
            continue
        car.exited_at = datetime.now()
        mycarpark.history = [*mycarpark.history, car]
        mycarpark.remove_car(car)

        clear_display()

        mycarpark.display_car_collection()

    elif choice == '5':
        clear_display()
        print("\nCar history")
        for car in mycarpark.history: 

            car.display_info()


print(f"\nGoodbye! See you soon.")






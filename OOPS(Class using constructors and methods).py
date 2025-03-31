#Class using constructors and methods
class Car:
    def __init__(self, brand, year_of_manufacturing, City):
        self.brand = brand
        self.year_of_manufacturing = year_of_manufacturing
        self.City = City

    def car_accessories(self, speaker):
        print(f'Hello, I am your new car. My name is {self.brand} from  {self.City} with {speaker} speakers')

Car1 = Car('volvo', 2021, 'Delhi')
print(Car1.brand, Car1.year_of_manufacturing, Car1.City)
Car1.car_accessories('Pioneer')

Car2 = Car('Maruti', 2020, "Ghaziabad")
#print(Car2.brand)
Car2.car_accessories('Sony')
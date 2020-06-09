class Vehicle:
    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        return self.__model.title()

    @model.setter
    def model(self, model):
        self.__model = model

    def __str__(self):
        return f'Model is {self.__model}'


class Car(Vehicle):
    def __init__(self, model, car_engine):
        super().__init__(model)
        self.__car_engine = car_engine

    @property
    def car_engine(self):
        return self.__car_engine.title()

    def __str__(self):
        return f'Model is {self.model} and car engine is {self.__car_engine}'


class Motorcycle(Vehicle):
    def __init__(self, model):
        super().__init__(model)


class CarRace:

    def __init__(self, name, cars):
        self.__cars = cars
        self.__name = name

    def __getitem__(self, item):
        return self.__cars[item]

    def __len__(self):
        return len(self.__cars)


if __name__ == '__main__':
    car = Car('Ferrari', 'V4')
    print(car.model)
    print(car.car_engine)
    print(car)

    motorcycle = Motorcycle('Harley')
    print(motorcycle.model)
    print(motorcycle)

    list_cars = [car]
    car_race = CarRace('Car race', list_cars)
    print(f'car race has {len(car_race)} cars ')
    for car in car_race:
        print(car)

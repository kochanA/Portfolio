from typing import List


class Car:
    DISCOUNT = .10

    def __init__(self, brand, model, year, color, power, engine_volume, price, max_gears):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.power = power
        self.engine_volume = engine_volume
        self.price = price
        self.max_gears = max_gears
        self.current_gear = 0
        self.is_turned_on = False

    @property
    def shortname(self):
        return f'{self.brand}-{self.model}-{self.color}'

    def start_engine(self):
        if self.is_turned_on:
            print(f'{self.shortname} is already turned on! You can break the engine!')
        else:
            print(f'Vroom! {self.shortname} is now turned on!')
            self.is_turned_on = True

    def stop_engine(self):
        if not self.is_turned_on:
            print(f'{self.shortname} is already turned off. Nothing to do.')
        else:
            print(f'{self.shortname} is now turned off!')
            self.is_turned_on = False

    def change_gear(self, amount):
        if -1 < self.current_gear + amount <= self.max_gears:
            self.current_gear += amount
        else:
            print(f'{self.shortname} has only {self.max_gears} gears. Operation not permited')

    def give_discount(self):
        self.price *= (1 - self.DISCOUNT)

    def __repr__(self):
        return f'[Car: {self.brand}, ' \
               f'{self.model}, ' \
               f'{self.year}, ' \
               f'{self.power}, ' \
               f'{self.engine_volume}, ' \
               f'{self.price}, ' \
               f'{self.max_gears}, ' \
               f'{self.current_gear}, ' \
               f'{self.is_turned_on}, ' \
               f'{self.shortname}]'

    def __add__(self, other):
        return self.price + other.price


class ElectricCar(Car):
    DISCOUNT = .15

    def __init__(self, brand, model, year, power, engine_volume, price, max_gears, range_km):
        super().__init__(brand, model, year, 'green', power, engine_volume, price, max_gears)
        self.range = range_km


class CarShop():
    def __init__(self, *args):
        self.cars: List[Car] = list(args)
        self.revenue = 0

    def add_car(self, car):
        self.cars.append(car)

    def sell_car(self, index, discount=False):
        try:
            car_for_sale = self.cars[index]
        except IndexError:
            print(f'There are only {len(self.cars)} available')
        else:
            if discount:
                car_for_sale.give_discount()
            self.revenue += car_for_sale.price
            self.cars.pop(index)

    def show_all_cars(self):
        print('All cars in shop:')
        for car in self.cars:
            print(car)

    def __repr__(self):
        return f'[CarShop: {self.cars}, {self.revenue}]'


if __name__ == '__main__':
    car1 = Car('Volvo', model='XC90', year=2015, color='white', power=160, engine_volume=2.0, price=150000, max_gears=6)
    car2 = Car('Fiat', model='Bravo', year=2009, color='black', power=150, engine_volume=1.4, price=20000, max_gears=6)
    electric = ElectricCar('Tesla', model='3', year=2021, power=350, engine_volume=3.0, price=300000, max_gears=6, range_km=300)

    print(car1 + car2)
    print(car1.shortname)
    car1.color = 'red'
    print(car1.color)
    print(car1.shortname)
    print('-'*20)
    shop = CarShop(car1, electric)
    shop.show_all_cars()
    shop.add_car(car2)
    electric.color = 'black'
    shop.show_all_cars()
    print('-' * 20)
    print(shop)
    shop.sell_car(2, True)
    print(shop)
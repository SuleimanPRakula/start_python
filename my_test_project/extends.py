class Transport:
    def __init__(self, max_speed, size):
        self.max_speed = max_speed
        self.size = size

    def move(self):
        print('Двигаться')

    def turn(self):
        print('Повернуть')

    def stop(self):
        print('Остановиться')

class Weapon:
    def __init__(self, callibre):
        self.callibre = callibre

    def action(self):
        print('Выстрел')


class Car(Transport):
    def __init__(self, max_speed, size, wheels_count, callibre):
        #super().__init__(max_speed, size)
        Transport.__init__(self, max_speed, size)
        Weapon.__init__(self, callibre)
        #super().__init__(max_speed,size)
        self.wheels_count = wheels_count

    def move(self):
        print('Ехать')

car = Car(120,2,4,9)
print(car.callibre)


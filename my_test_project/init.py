class Person:
    def __init__(self, name):
        self.__person_name = name

    def __get_name(self):
        return self.__person_name

    def __set_name(self, name):
        self.__person_name = name
    
    name = property(__get_name, __set_name)


class Car:
    def __init__(self, model):
        self.__car_model = model

#    @property
#    def model(self):
#        return self.__car_model

    model = property()

    @model.setter
    def model(self,model):
        self.__car_model = model


class Reactor:
    def __init__(self, max_power=9000):
        self.__cur_power = 0
        self.max_power = max_power
        
    def __get_power(self):
        return self.__cur_power

    def __set_power(self, power):
        if power > self.max_power:
            print (f'Ты што дибил, щас все жахнет! Ahtung!Ahtung! Максималка {self.max_power}')
            self.__cur_power = self.max_power
            return

        self.__cur_power = power
        return

    power = property(__get_power, __set_power)

reactor = Reactor()

print(reactor.power)
reactor.power = 150000
print(reactor.power)
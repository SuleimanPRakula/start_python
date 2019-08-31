class Controller:
    def start(self):
        pass
    
    def move_right(self,velocity):
        pass

    def move_left(self,velocity):
        pass

    def stop(self):
        pass

class Arduino(Controller):
    def start(self):
        print('Arduino start')
    
    def move_right(self,velocity):
        print(f'Arduino right {velocity}')

    def move_left(self,velocity):
        print(f'Arduino left {velocity}')

    def stop(self):
        print('Arduino stop')

class Raspberry(Controller):
    def start(self):
        print('Raspberry start')

    def move_right(self,velocity):
        print(f'Raspberry right velocity: {velocity}')

    def move_left(self,velocity):
        print(f'Raspberry left velocity: {velocity}')

    def stop(self,velocity):
        print('Raspberry stop')

class Device:
    def __init__(self,serial,press):
        self.serial = serial
        self.press = press
    
    def start_press(self):
        self.press.start()

    def increase_pressure(self,velocity):
        self.press.move_right(velocity)

    def decrease_pressure(self,velocity):
        self.press.move_left(velocity)

    def stop_press(self):
        self.press.stop()
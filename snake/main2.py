from classes2 import Device, Arduino, Raspberry
from exampe_tuple import uim

arduino = Arduino()

device = Device(625000, uim)

device.start_press()
device.increase_pressure(5)
device.decrease_pressure(5)
device.stop_press()
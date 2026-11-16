import smbus
import time

bus = smbus.SMBus(1)
ADDRESS = 0x68

bus.write_byte_data(ADDRESS, 0x6B, 0)

while True:
    x = bus.read_byte_data(ADDRESS, 0x3B)
    y = bus.read_byte_data(ADDRESS, 0x3D)
    z = bus.read_byte_data(ADDRESS, 0x3F)

    print("X:", x, "Y:", y, "Z:", z)

    time.sleep(0.1)

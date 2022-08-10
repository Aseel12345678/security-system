# Add your Python code here. E.g.
from microbit import *
pin2.write_digital(0)
pin0.write_digital(0)
while True:
    motion = pin1.read_digital()
    if motion:
        pin2.write_digital(1)
        pin0.write_digital(1)
    else:
        pin2.write_digital(0)
        pin0.write_digital(0)
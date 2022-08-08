# Add your Python code here. E.g.
from microbit import *
pin1.write_digital(0)
pin0.write_digital(0)
while True:
    if pin2.read_digital():
        pin1.write_digital(1)
        pin0.write_digital(1)
    

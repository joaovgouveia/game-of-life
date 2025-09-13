from automata import Plate
from time import sleep
from random import randint
import os

clear_cmd = "cls" if os.name == 'nt' else 'clear'

def build_plate() -> Plate:
    plate = Plate((64,32), rules=(2, 3, 4))
    for _ in range(600):
        plate.set_cell((randint(0, 31), randint(0, 63)), True)
    return plate

if __name__ == "__main__":
    plate = build_plate()
    step = 0
    while True:
        os.system(clear_cmd)
        print(plate)
        print(f"step: {step}")
        if plate.updated == False: break
        plate.next_state()
        step += 1 
        sleep(0.1)
    

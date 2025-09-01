from automata import Plate
from time import sleep
import os

clear_cmd = "cls" if os.name == 'nt' else 'clear'

def build_plate() -> Plate:
    plate = Plate((32,32))
    plate.set_cell((0,2), True)
    plate.set_cell((1,2), True)
    plate.set_cell((2,2), True)
    plate.set_cell((1,0), True)
    plate.set_cell((2,1), True)
    plate.set_cell((30,30), True)
    plate.set_cell((30,31), True)
    plate.set_cell((31,30), True)
    plate.set_cell((31,31), True)
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
    
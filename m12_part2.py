"""Mission 12 part 2 sequence.python -lift tree--version

Moves forward and in a diagonal position, it lifts up the tree.
"""
from base_robot import PybricksBot
from pybricks.tools import wait

def run_mission_12_2():
    bot = PybricksBot()
    try:
        print("[Mission 12 Part 2] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence    
    bot.drive_forward(47, 250)
    bot.turn_right(36, 90) 
    bot.drive_forward(4, 100)
    bot.move_left_arm(-90, 90)
    bot.move_left_arm(29, 90)
    bot.turn_left(35,100)
    bot.drive_backward(50, 550)
    
    try:
        print("[Mission 12 Part 2] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_12_2()

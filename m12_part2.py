"""Mission 12 part 2 sequence.python -lift tree--version

Moves forward and in a diagonal position, it lifts up the tree.
"""
from base_robot import PybricksBot
from pybricks.tools import wait

def run_mission_12():
    bot = PybricksBot()
    try:
        print("[Mission 12] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence    
    bot.drive_forward(47, 250)
    bot.turn_right(45, 90) 
    bot.drive_forward(4, 100)
    bot.move_left_arm(-99, 100)
    bot.move_left_arm(29, 100)
    bot.turn_left(35,100)
    bot.drive_backward(50, 550)
    
    try:
        print("[Mission 12] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_12()

"""Mission 3 sequence.python --version

Stub mission grouped for menu option 4. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_03_02():
    bot = PybricksBot()
    try:
        print("[Mission 03 Part 2] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence
    
    bot.drive_forward(50, 300)
    bot.drive_backward(50, 250)#mission 3 ends
    wait(6000)
    bot.drive_forward(6.56, 200)#mission 2 starts
    bot.turn_right(40, 100)
    bot.drive_forward(25, 200)
    bot.move_right_arm(200, 150)#lifting the seed
    bot.drive_backward(10, 200)
    bot.turn_right(35, 150)
    bot.drive_forward(35, 250)
    bot.turn_left(40, 150)
    bot.drive_forward(19, 250)
    bot.turn_right(30, 150)
    bot.move_right_arm(-260, 250)
    bot.drive_forward(28, 200)
    bot.turn_left(20, 100)
    bot.move_right_arm(140, 150)#picking up second seed 
    bot.turn_right(50, 150)
    bot.drive_forward(80, 300)
    try:
        print("[Mission 03 Part 2] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_03_02()
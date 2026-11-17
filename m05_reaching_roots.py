"""Mission 5 sequence.python --version

Stub mission grouped for menu option 5. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_05():
    bot = PybricksBot()
    try:
        print("[Mission 05] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence
    
    bot.move_right_arm(-430, 500)
    bot.drive_forward(57, 250)
    bot.move_right_arm(210, 1000)
    wait(100)
    bot.drive_backward(9, 200)
    bot.move_right_arm(-200, 1000)
    bot.drive_forward(9, 200)
    bot.move_right_arm(400, 1000)
    bot.drive_backward(57, 400)
    #bot.turn_left(28, 150)
    #bot.drive_forward(10, 200)
    #bot.move_left_arm(70, 150)
    #bot.drive_backward(6, 150)
    #bot.move_left_arm(-80, 150)
    #bot.drive_backward(6, 150)
    #bot.move_left_arm(-50, 150)
    try:
        print("[Mission 05] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_05()

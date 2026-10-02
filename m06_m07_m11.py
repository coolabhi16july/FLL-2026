"""Mission 3 sequence.python --version

Stub mission grouped for menu option 4. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_10():
    bot = PybricksBot()
    try:
        print("[Mission 6_7] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence
    bot.drive_forward(40, 200)
    bot.turn_right(47, 100)
    bot.drive_forward(43, 200)
    bot.turn_left(65, 75)
    bot.drive_forward(10, 100)
    bot.drive_backward(2, 100)
    bot.turn_left(50, 100)
    bot.drive_backward(37, 100)
    #bot.drive_forward(5.5, 150)
    #bot.turn_left(37, 150)
    #bot.drive_forward(65, 200)

    #bot.move_right_arm(-70, 121)
    #bot.drive_forward(35, 200)
    #bot.move_right_arm(170, 312)
    #bot.drive_forward(2, 250)
    #bot.turn_left(28, 100)
    #bot.drive_forward(35, 250)
    #bot.move_right_arm(35, 300)

    
    try:
        print("[Mission 6_7] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_10()
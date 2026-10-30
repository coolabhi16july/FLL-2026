"""Mission 3 sequence.python --version

Stub mission grouped for menu option 4. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_10():
    bot = PybricksBot()
    try:
        print("[Mission 3] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence
    
    bot.drive_forward(75.25, 250)
    bot.move_right_arm(475, 550)
    #bot.turn_left(28, 150)
    #bot.drive_forward(10, 200)
    #bot.move_left_arm(70, 150)
    #bot.drive_backward(6, 150)
    #bot.move_left_arm(-80, 150)
    #bot.drive_backward(6, 150)
    #bot.move_left_arm(-50, 150)
    try:
        print("[Mission 3] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_10()

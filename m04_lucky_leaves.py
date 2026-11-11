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
    
    bot.drive_forward(67, 275)
    wait(500)
    bot.turn_left(32, 150)
    bot.drive_forward(10, 100)
    bot.move_right_arm(200, 100)
    bot.drive_backward(20, 175)
    bot.turn_right(45, 150)
    bot.drive_backward(75, 400)
    wait(7000)
    bot.drive_forward(70, 200)
    bot.turn_left(42.5, 150)
    bot.drive_forward(5, 100)
    bot.move_right_arm(-200, 150)
    bot.drive_backward(15, 100)
    bot.turn_right(60, 150)
    bot.drive_backward(70, 300)

    try:
        print("[Mission 3] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_10()

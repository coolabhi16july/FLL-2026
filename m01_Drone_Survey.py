"""Mission 1 sequence.python --version

Stub mission grouped for menu option 4. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_01():
    bot = PybricksBot()
    try:
        print("[Mission 01] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence
    bot.drive_forward(75.5, 300)
    wait(100)
    bot.turn_left(15, 200)
    wait(50)
    bot.drive_forward(2.55, 210)
    bot.turn_left(35, 350)
    bot.turn_right(30, 150)
    bot.drive_backward(65, 500)
    try:
        print("[Mission 1] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_01()
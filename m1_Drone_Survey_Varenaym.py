"""Mission 3 sequence.python --version

Stub mission grouped for menu option 4. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_10():
    bot = PybricksBot()
    try:
        print("[Mission 1] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence
    bot.drive_forward(74, 200)
    bot.turn_left(15, 100)
    bot.drive_forward(2, 200)
    bot.turn_left(30, 150)
    bot.turn_right(45, 150)
    bot.drive_backward(65, 500)
    try:
        print("[Mission 1] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_10()
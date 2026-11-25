"""Mission 2 sequence.python --version

Stub mission grouped for menu option 2. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_02():
    bot = PybricksBot()
    try:
        print("[Mission 02] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence

    bot.drive_forward(6.56, 200)#mission 2 starts
    bot.turn_right(40, 100)
    bot.drive_forward(27, 200)
    bot.move_right_arm(200, 150)#lifting the seed
    bot.drive_backward(60, 400)
    try:  
        print("[Mission 02] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_02()

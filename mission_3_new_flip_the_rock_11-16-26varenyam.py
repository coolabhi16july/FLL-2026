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
    try:
        print("[Mission 03 Part 2] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_03_02()
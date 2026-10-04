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
    
    bot.drive_forward(50, 300)
    bot.drive_backward(50, 250)
    wait(5000)
    bot.drive_forward(6.56, 200)
    bot.turn_right(40, 100)
    bot.drive_forward(32, 200)
    bot.move_right_arm(300, 150)
    bot.drive_backward(40, 200)
    try:
        print("[Mission 3] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_10()

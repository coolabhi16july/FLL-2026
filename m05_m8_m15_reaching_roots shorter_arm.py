"""Mission 5 sequence.python --version

Stub mission grouped for menu option 5. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_05_08_15():
    bot = PybricksBot()
    try:
        print("[Mission 05] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence
    
    bot.move_right_arm(-430, 500)
    bot.drive_forward(67, 250)
    bot.move_right_arm(210, 1000)
    wait(100)
    bot.drive_backward(9, 1500)
    bot.move_right_arm(-200, 1000)
    bot.drive_forward(9, 200)
    bot.move_right_arm(400, 1000)
    bot.drive_backward(1.5, 150)
    wait(300)
    # Mission 8: Tangle sequence
    bot.turn_right(77.5, 150)
    bot.drive_forward(24.5, 150)
    wait(50)
    bot.turn_left(70, 150)
    bot.drive_forward(30, 560)
    wait(1000)
    bot.drive_backward(1, 150)
    bot.drive_forward(15, 560)
    wait(1000)
    bot.drive_backward(1.5, 150)
    bot.drive_forward(10, 560)
    wait(1000)
    bot.drive_backward(15, 150)
    bot.move_right_arm(-200,200)
    
    try:
        print("[Mission 05_08_15] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_05_08_15()
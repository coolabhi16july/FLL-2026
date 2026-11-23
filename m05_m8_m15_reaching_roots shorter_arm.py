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
    bot.drive_forward(60, 250)
    bot.move_right_arm(210, 500)
    wait(100)
    bot.drive_backward(4, 200)
    bot.move_right_arm(-200, 500)
    bot.drive_forward(4, 200)
    bot.move_right_arm(400, 500)
    bot.drive_backward(1, 150)
    wait(300)
    # Mission 8: Tangle sequence
    bot.turn_right(76, 150)
    bot.drive_forward(26.5, 150)
    wait(50)
    bot.turn_left(76, 150)

    # bot.move_right_arm(-325, 200) # Arm goes down to grab the root
    # bot.drive_forward(6, 100)
    # bot.move_right_arm(300, 200)
    # bot.turn_right(7, 100)
    # bot.drive_backward(6, 100)
    # bot.turn_left(7, 100)
    # wait(5000)

    
    bot.drive_forward(20, 560)
    wait(1000)
    bot.drive_backward(2, 150)
    bot.drive_forward(18, 560)
    #wait(5000)
    #bot.drive_backward(10, 150)
    #bot.drive_forward(15, 560)
    #wait(5000)
    #bot.move_right_arm(250, 350)
    #bot.turn_right(10, 200)
    bot.drive_backward(15, 100)
    #bot.turn_left(45, 200)
    try:
        print("[Mission 05_08_15] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_05_08_15()
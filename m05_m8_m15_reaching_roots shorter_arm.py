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
    bot.drive_backward(9, 200)
    bot.move_right_arm(-200, 1000)
    bot.drive_forward(9, 200)
    bot.move_right_arm(400, 1000)
    bot.drive_backward(1.5, 200)
    wait(300)
    # Mission 8: Tangle sequence
    bot.turn_right(77.5, 150)
    bot.drive_forward(23.5, 200)
    bot.turn_left(70, 150)
    bot.drive_forward(30, 560)
    wait(1000)
    bot.drive_backward(1, 200)
    bot.drive_forward(15, 560)
    wait(1000)
    bot.drive_backward(1.5, 200)
    bot.drive_forward(10, 560)
    wait(1000)
    bot.drive_backward(15, 200)
    bot.move_right_arm(-200,200)
    ##bot.drive_backward(5, 200)
    #bot.turn_right(33, 50)
    #bot.drive_forward(20, 200)
    #bot.move_right_arm(200, 1000)
    #bot.drive_backward(15, 200)
    #bot.turn_right(45, 150)
    #bot.drive_forward(60, 200)
    #bot.drive_backward(5, 100)
    #bot.turn_right(71, 150)
    #bot.drive_forward(27 , 200)
    #bot.turn_left(110, 150)
    #bot.move_right_arm(-280, 300)
    #bot.turn_left(10, 150)
    #bot.move_right_arm(-60, 100)
    #bot.move_right_arm(130, 200)
    #wait(1000)
    #bot.turn_right(30, 200)
    #bot.drive_forward(50, 300)
    #bot.turn_right(45, 200)
    #bot.drive_forward(60, 400)
    
    try:
        print("[Mission 05_08_15] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_05_08_15()
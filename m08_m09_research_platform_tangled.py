"""Mission 5 sequence.python --version

Stub mission grouped for menu option 5. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_08_09():
    bot = PybricksBot()
    try:
        print("[Mission 08 and 09] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass
    # TODO: implement real sequence
    bot.drive_forward(60, 250)
    # Mission 8: Tangle + Research platform sequence
    bot.turn_right(75, 150)
    bot.drive_forward(27, 150)
    wait(50)
    bot.turn_left(78, 150)
    #Facing the research platform 
    bot.move_right_arm(-375, 200) #Arm down to pick up the tangled platform
    bot.drive_forward(20, 560) #
    wait(1000)
    bot.drive_backward(5, 100)
    wait(1000)
    #bot.drive_forward(20, 560)
    bot.move_right_arm(320, 400) #Arm up to lift the tangled vined
    bot.drive_backward(5, 100)
    wait(1000)
    #bot.move_right_arm(300, 200)
    bot.turn_right(20, 100)
    bot.drive_backward(30, 300)
    bot.turn_right(15, 100)
    bot.drive_backward(70, 560)
    try:
        print("[Mission 08_09] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_08_09()
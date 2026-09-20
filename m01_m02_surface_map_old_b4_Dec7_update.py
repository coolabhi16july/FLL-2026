"""Mission 1 & 2 (Surface Map)."""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_1_2():
    """Run the Surface Map mission (menu option 1)."""

    # 1. Setup (keep these lines)
    bot = PybricksBot()
    try:
        print("[Mission 1_2] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass
    try:
        bot.home_arms()
        wait(300)
    except Exception:
        pass

    # 2. Mission steps (edit these lines with your moves!)
    # launching from red base 
    bot.drive_forward(63,300)
    wait(100)

    bot.turn_left(31, 200)
    wait(100)
    

    bot.drive_forward(19, 200)
    # goes toward mission 2


    wait(100)

    bot.move_right_arm(400, 100)
    # lifting artifact, mission 2 
    wait(100)

    bot.drive_backward(13, 100)
    wait(500)

    bot.turn_right(46, 70)
    wait(1500)


    bot.move_left_arm(200, 500)
    wait(100)
    # grabbing artifact, mission 1
    bot.move_left_arm(-200, 300)
    wait(100)


    # bot.
    bot.drive_backward(35, 750)

    bot.turn_right(20, 300)

    bot.drive_backward(19, 250)

    # 3. Finish (keep these lines)
    try:
        print("[Mission 1_2] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_1_2()
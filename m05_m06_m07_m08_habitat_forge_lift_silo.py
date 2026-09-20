"""Mission 5, 6, 7 & 8 (Habitat / Forge / Lift / Silo) sequence.

Stub mission grouped for menu option 4. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_5_6_7_8():
    bot = PybricksBot()
    try:
        print("[Mission 5_6_7_8] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence
    bot.right_arm_motor.reset_angle(0)
    bot.drive_forward(27)
    bot.move_right_arm(100,1000)
    bot.move_right_arm(-340,1000)
    bot.move_right_arm(340,1000)
    bot.move_right_arm(-340,1000)
    bot.move_right_arm(340,1000)
    bot.move_right_arm(-340,1000)
    bot.move_right_arm(340,1000)
    bot.turn_left(9)
    bot.drive_forward(31)
    bot.turn_right(56)
    bot.move_left_arm(-350,300)
    bot.drive_forward(12)
    bot.move_left_arm(580,700)
    bot.turn_right(30)
    bot.turn_left(5)
    bot.drive_backward(1)
    bot.turn_left(40)
    bot.drive_forward(4)
    bot.turn_left(23)
    bot.turn_right(5)
    bot.drive_backward(40,700)
    bot.turn_left(30)
    bot.drive_backward(30,700)

    
    try:
        print("[Mission 5_6_7_8] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_5_6_7_8()
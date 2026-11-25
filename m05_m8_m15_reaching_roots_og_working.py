"""Mission 5 sequence.python --version

Stub mission grouped for menu option 5. Replace placeholder steps with
actual mission logic.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_05_08_15():
    bot = PybricksBot()
    try:
        print("[Mission 05_15] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

            # TODO: implement real sequence
    
    bot.move_right_arm(-430, 500)
    bot.drive_forward(60, 250)
    bot.move_right_arm(210, 1000) # Move Right Arm up to flip the reaching roots
    bot.drive_backward(9, 200)
    bot.move_right_arm(-220, 1000) # Move Right Arm down to grab the root
    bot.drive_forward(9, 200)
    bot.move_right_arm(400, 1000) # 2nd flick to flip the reaching roots
    # Mission 8: Tangle sequence
    bot.drive_backward(2, 200)
    wait(50)
    bot.turn_right(75 , 150)
    bot.drive_forward(60, 200) # Pushing the skylight in Biocentric
    bot.drive_backward(5, 100)
    bot.turn_right(71, 150)
    bot.drive_forward(28 , 200)
    bot.turn_left(105, 150)# angling the robot o the garbage hatch and the skyroof
    bot.move_right_arm(-315, 300)
    bot.turn_left(7.5, 150)
    bot.drive_forward(2, 150)
    bot.move_right_arm(-60, 100)
    bot.move_right_arm(300, 300)
    wait(1000)
    bot.turn_right(17.5, 200)
    bot.drive_forward(35, 400)
    bot.turn_right(20, 200)
    bot.drive_forward(70, 500)
    
    try:
        print("[Mission 05_15] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_05_08_15()
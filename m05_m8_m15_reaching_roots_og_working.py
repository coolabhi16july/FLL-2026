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
    bot.drive_forward(59, 250)
    bot.move_right_arm(210, 1000) # Move Right Arm up to flip the reaching roots
    bot.drive_backward(9, 200)
    bot.move_right_arm(-220, 1000) # Move Right Arm down to grab the root
    bot.drive_forward(9, 200)
    bot.move_right_arm(400, 1000) # 2nd flick to flip the reaching roots
    bot.drive_backward(2, 200)
    # Mission 8: Tangle sequence
    bot.move_right_arm(-225, 150)
    wait(2000)
    bot.turn_right(30, 50)
    bot.drive_forward(15, 150) # Move Forward push the BioCentric solar panel
    bot.move_right_arm(210, 200) # Move Right Arm up to move the vine root
    bot.drive_backward(15, 200)
    wait(1000)
    bot.turn_right(40, 150)
    bot.drive_forward(60, 200) # Pushing the skylight in Biocentric
    bot.drive_backward(5, 100)
    bot.turn_right(71, 150)
    bot.drive_forward(28 , 200)
    bot.turn_left(110, 150)
    bot.move_right_arm(-275, 300)
    bot.turn_left(10, 150)
    bot.drive_forward(3, 200)
    bot.move_right_arm(-60, 100)
    bot.move_right_arm(150, 200)
    wait(1000)
    bot.turn_right(15, 200)
    bot.drive_forward(40, 400)
    bot.turn_right(25, 200)
    bot.drive_forward(70, 400)
    
    try:
        print("[Mission 05_08_15] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_05_08_15()
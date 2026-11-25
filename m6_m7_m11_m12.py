"""Mission 6&11 sequence.python --version


Stub mission grouped for menu option 4. Replace placeholder steps with
actual mission logic.
"""


from base_robot import PybricksBot
from pybricks.tools import wait



def run_combined_missions_06_07_11():
    bot = PybricksBot()
    try:
        print("[Mission 6, Mission 7 and Mission 11] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass


    # TODO: implement real sequence
    bot.move_left_arm(570, 500)
    bot.drive_forward(64, 267)
    bot.move_left_arm(-600, 600)
    bot.move_left_arm(400, 500)
    bot.drive_backward(5,25)
    bot.move_left_arm(-550, 500)
    bot.turn_left(70,125)
    bot.drive_forward(37, 125)
    bot.turn_left(27, 150)
    bot.drive_backward(15, 108)    
    bot.drive_forward(4, 150)
    bot.turn_left(97, 100)
    bot.drive_forward(52, 200)
    bot.turn_right(27,102)
    bot.drive_forward(50,300)   
    
    try:
        print("[Mission 6, Mission 7 and Mission 11] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass

        
if __name__ == "__main__":
    run_combined_missions_06_07_11()

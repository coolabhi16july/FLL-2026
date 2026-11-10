"""Mission 6&11 sequence.python --version


Stub mission grouped for menu option 4. Replace placeholder steps with
actual mission logic.
"""


from base_robot import PybricksBot
from pybricks.tools import wait




def run_mission_10():
    bot = PybricksBot()
    try:
        print("[Mission 1] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass


            # TODO: implement real sequence
    bot.move_left_arm(570, 502)
    bot.drive_forward(65, 267)
    bot.move_left_arm(350, 502)
    bot.drive_backward(10,100)
    bot.move_left_arm(-550, 502)
    bot.turn_left(75,125)
    bot.drive_forward(40, 125)
    bot.turn_left(27, 152)
    bot.drive_backward(16, 72)    
    bot.drive_forward(1, 150)
    bot.turn_left(95, 100)
    bot.drive_forward(40,250)
    bot.turn_right(25,102)
    bot.drive_forward(50,300)

    
    # bot.move_left_arm(110, 75)
    # bot.turn_left(90, 125)
    # bot.drive_forward(40, 125)
    # bot.turn_right(15, 75)
    # bot.drive_forward(40, 125)
   





    #
    #
    #
    #bot.drive_backward(2,25)
    #bot.turn_right(94,50)
    #bot.drive_forward(27,125)
    #bot.turn_right(170,75)
    #bot.drive_forward(35,125)
    #bot.drive_backward(5, 25)
    #bot.turn_right(45,50)
    #bot.drive_forward(18, 100)
    #bot.turn_left(91,50)
    #bot.drive_backward(42,100)
    #bot.turn_right(114,50)
    #bot.drive_forward(68,150)
    try:
        print("[Mission 1] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass




if __name__ == "__main__":
    run_mission_10()




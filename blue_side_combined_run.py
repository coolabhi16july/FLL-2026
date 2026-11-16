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
    bot.drive_forward(66, 267)
    bot.move_left_arm(-400, 500)
    bot.move_left_arm(350, 500)
    bot.drive_backward(5,25)
    bot.move_left_arm(-550, 500)
    bot.turn_left(70,125)
    bot.drive_forward(37, 125)
    bot.turn_left(27, 150)
    bot.drive_backward(15, 108)    
    bot.drive_forward(2, 150)
    bot.turn_left(95, 100)
    bot.drive_forward(30, 200)
       
    
    try:
        print("[Mission 6, Mission 7 and Mission 11] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass

def run_mission_12():
    bot = PybricksBot()
    try:
        print("[Mission 12] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass


    # TODO: implement real sequence
    bot.drive_forward(34, 150)
    bot.move_right_arm(100, 100)
    bot.drive_backward(17, 100)
    bot.turn_left(7, 50)
    bot.move_right_arm(-110, 100)
    bot.drive_backward(25, 250)
    bot.wait(5000)

    try:
        print("[Mission 12] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass

def run_mission_12_part2():
    bot = PybricksBot()
    try:
        print("[Mission 12 Part 2] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass

    # TODO: implement real sequence    
    bot.drive_forward(47, 250)
    bot.turn_right(36, 90) 
    bot.drive_forward(4, 100)
    bot.move_left_arm(-90, 90)
    bot.move_left_arm(29, 90)
    bot.turn_left(35,100)
    bot.drive_backward(50, 550)
    bot.wait(5000)
    
    try:
        print("[Mission 12 Part 2] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass
        
if __name__ == "__main__":
    run_combined_missions_06_07_11()
    run_mission_12()
    run_mission_12_part2()  




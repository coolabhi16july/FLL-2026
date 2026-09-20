"""Mission 3, 13 & 9 (Mineshaft / Statue / Market)."""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_3_13_9():
    """Run the Mineshaft / Statue / Market mission (menu option 3)."""

    # 1. Setup (keep these lines)
    bot = PybricksBot()
    try:
        print("[Mission 3_13_9] Starting")
        bot.hub.speaker.beep()
    except Exception:
        pass
    try:
        bot.home_arms()
        wait(300)
    except Exception:
        pass

    # 3. Mission steps (edit these lines with your moves!)
    # TODO: replace the sample moves below with the real mission path.
    bot.drive_forward(67, 200)
    bot.turn_right(27.5, 200)
    #when turning touches the mission model 
    bot.drive_forward(13, 200)
    bot.turn_right(21, 200)
    bot.move_left_arm(-500, 500)   
    bot.drive_forward(8, 200)
    # after reaching the mission model, move right arm to raise the lever
    # bot.move_right_arm(-100, 200)
    # bot.move_right_arm(100, 200)
    # raise left arm to grab artifact
    bot.move_left_arm(500, 200)
    wait(200)
    bot.move_left_arm(-125, 200)
    bot.drive_backward(8, 200)

    #### Mission 9 Starts
    bot.turn_right(17, 200)# Turn toward statue rebuild
    bot.drive_forward(22, 200)
    bot.turn_right(10, 200)
    bot.move_left_arm(-245, 200) #lower left arm to lift statue
    bot.drive_forward(8, 200)   
    bot.move_left_arm(200, 200)
    bot.turn_left(42, 50)
    bot.turn_right(6, 200)
    ### Mission 9 Complete and come backward and turn left to go for Mission 13
    bot.drive_backward(16, 200)
    bot.move_left_arm(150)
   
   ## Mission 13 Attempt Start - Kirti, Anil -11/22
    bot.turn_left(23, 50)
    bot.drive_forward(67, 300)
    bot.turn_right(23, 200)
    bot.drive_forward(35, 400)
    bot.drive_backward(9)
    ## Mission 13 Completed and robot came backward

    ## Mission 10 Starts
    bot.turn_left(21, 150)
    bot.drive_backward(11, 200)
    bot.turn_right(25, 150)
    #bot.drive_forward(15, 200)
    bot.move_left_arm(-250)
    bot.move_left_arm(150)
    bot.drive_backward(10)
    ## Mission 10 Completed and robot came backward
    bot.turn_right(17, 150)
    bot.drive_forward(58, 200)
    bot.turn_left(65, 150)
    bot.drive_forward(90, 500)

    # 3. Finish (keep these lines)
    try:
        print("[Mission 3_13_9] Complete")
        bot.hub.speaker.beep(frequency=1000, duration=200)
    except Exception:
        pass


if __name__ == "__main__":
    run_mission_3_13_9()

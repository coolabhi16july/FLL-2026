<<<<<<< HEAD
# FLL-2026
Green Storm gear Python code 
=======
# Our SPIKE Prime Robot Guide

This project holds all of the Python code we use for FIRST LEGO League robot
missions. Everything is written in Pybricks and meant for ages 10–13. Keep it
fun, keep it simple, and show what you know!

## Robot setup (Ports)

- Left wheel motor → Port D
- Right wheel motor → Port C
- Right arm motor → Port A
- Left arm motor → Port E

The wheels are 62 mm across and the space between them (axle track) is 140 mm.
If we change the build, we update those numbers in `base_robot.py`.

## Running the mission menu

1. Connect to the hub with Pybricks (USB or Bluetooth).
2. Download and run `mission_menu.py`.
3. On the hub, tap LEFT or RIGHT to pick a mission number.
4. Press the CENTER button once to start the mission.
5. After the mission finishes, the menu comes back automatically.

### Menu order and mission files

| Menu Number | Missions covered | Python file name                         |
|-------------|------------------|------------------------------------------|
| 1           | Missions 1 & 2   | `m01_m02_surface_map.py`                  |
| 2           | Missions 11 & 12 | `m11_m12_angler_salvage.py`               |
| 3           | Missions 3, 13, 9| `m03_m13_m09_mineshaft_statue_market.py`  |
| 4           | Missions 5,6,7,8 | `m05_m06_m07_m08_habitat_forge_lift_silo.py` |
| 5           | Missions 10      | `m10_scales.py`                          |

## Adding a new mission to the menu

1. Copy an existing mission file (like `m01_m02_surface_map.py`).
2. Change the moves inside the `run_mission_*` function.
3. Save the file with a new name (for example `m10_new_goal.py`).
4. Open `mission_menu.py` and add your new function to the mission list.
5. Download `mission_menu.py` again so the hub has the latest missions.

## What judges might ask (and quick answers)

- **How do you choose which mission to run?** We run `mission_menu.py`, use the
	LEFT and RIGHT buttons to pick a number, and press CENTER to start it.
- **How do you make the robot move straight?** Our `PybricksBot` class in
	`base_robot.py` uses the hub’s gyro to keep the wheels going straight.
- **How do you reset the arms?** Each mission calls `bot.home_arms()` at the
	start so both attachments return to their zero position.
- **What happens if we change the robot build?** We update the port numbers and
	wheel sizes in `base_robot.py`, and all missions keep working.
- **How do you add new missions?** We make a new mission file with a
	`run_mission_*` function and add it to the dictionary in `mission_menu.py`.

## File checklist

- `mission_menu.py` → hub menu using `hub_menu` (official Pybricks helper).
- `base_robot.py` → shared robot code (motors, arms, homing, turns).
- `m01_m02_surface_map.py` etc. → individual missions that call `PybricksBot`.

Keep coding, keep testing, and have fun on the mission table!

>>>>>>> 9aca7e9 (Adding 2025 code)

"""Mission 13 Deliver artifact.

Refactored into a callable so the mission menu can trigger it without
executing code at import time.
"""

from base_robot import PybricksBot
from pybricks.tools import wait


def run_mission_13():
	"""Execute Mission 13 & deliver artifacts.

	Adjust speeds/angles as needed during tuning. Repeated forward/backward
	cycles preserved; consider consolidating with a helper if you change pattern.
	"""
	bot = PybricksBot()
	# Start cue
	bot.drive_forward(20, 200)
	bot.turn_right(42, 150)
	bot.drive_forward(30, 200)
	bot.move_right_arm(-325, 300)
	bot.turn_right(8, 150)
	bot.move_right_arm(325, 500)
	bot.drive_backward(50, 500)


	# End cue
	try:
		print("[Mission 13] Complete")
		bot.hub.speaker.beep(frequency=1000, duration=200)
	except Exception:
		pass


if __name__ == "__main__":
	run_mission_13()

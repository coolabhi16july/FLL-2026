"""Extra robot helpers that are not currently used by the missions."""

from pybricks.tools import wait

from base_robot import (
    PybricksBot,
    _clamp,
    _normalize_heading,
    LEFT_ARM_DIRECTION,
    LEFT_ARM_GEAR_RATIO,
    MAX_ARM_SPEED_DEG_S,
    MAX_TURN_RATE_DEG_S,
    RIGHT_ARM_DIRECTION,
    RIGHT_ARM_GEAR_RATIO,
)


def turn_in_place(bot: PybricksBot, angle, speed=150):
    """Force a pivot by running wheels in opposite directions."""

    turn_rate = _clamp(speed, -MAX_TURN_RATE_DEG_S, MAX_TURN_RATE_DEG_S)
    direction = 1 if angle >= 0 else -1
    bot.left_drive_motor.run(direction * turn_rate)
    bot.right_drive_motor.run(-direction * turn_rate)

    start_heading = bot.hub.imu.heading()
    while abs(_normalize_heading(bot.hub.imu.heading() - start_heading)) < abs(angle):
        wait(10)

    bot.left_drive_motor.stop()
    bot.right_drive_motor.stop()


def move_right_arm_by(bot: PybricksBot, arm_degrees, speed=200):
    """Move the right arm by physical ``arm_degrees`` using gear ratio."""

    motor_degrees = RIGHT_ARM_DIRECTION * arm_degrees * RIGHT_ARM_GEAR_RATIO
    bot.move_right_arm(motor_degrees, speed=speed)


def move_left_arm_by(bot: PybricksBot, arm_degrees, speed=200):
    """Move the left arm by physical ``arm_degrees`` using gear ratio."""

    motor_degrees = LEFT_ARM_DIRECTION * arm_degrees * LEFT_ARM_GEAR_RATIO
    bot.move_left_arm(motor_degrees, speed=speed)


def move_right_arm_to(bot: PybricksBot, arm_degrees_target, speed=200):
    """Move the right arm to an absolute angle (requires prior homing)."""

    target_motor = RIGHT_ARM_DIRECTION * arm_degrees_target * RIGHT_ARM_GEAR_RATIO
    try:
        current_motor = bot.right_arm_motor.angle()
    except AttributeError:
        current_motor = 0
    delta = target_motor - current_motor
    bot.move_right_arm(delta, speed=speed)


def move_left_arm_to(bot: PybricksBot, arm_degrees_target, speed=200):
    """Move the left arm to an absolute angle (requires prior homing)."""

    target_motor = LEFT_ARM_DIRECTION * arm_degrees_target * LEFT_ARM_GEAR_RATIO
    try:
        current_motor = bot.left_arm_motor.angle()
    except AttributeError:
        current_motor = 0
    delta = target_motor - current_motor
    bot.move_left_arm(delta, speed=speed)


def run_wheels(bot: PybricksBot, left_speed, right_speed, duration_ms=500):
    """Run wheel motors at raw speed (deg/s) for diagnostics."""

    left = _clamp(left_speed, -MAX_ARM_SPEED_DEG_S, MAX_ARM_SPEED_DEG_S)
    right = _clamp(right_speed, -MAX_ARM_SPEED_DEG_S, MAX_ARM_SPEED_DEG_S)
    bot.left_drive_motor.run(left)
    bot.right_drive_motor.run(right)
    wait(duration_ms)
    bot.left_drive_motor.stop()
    bot.right_drive_motor.stop()


def test_drive_motors(bot: PybricksBot, speed=300, duration_ms=500):
    """Pulse wheels forward then backward to confirm wiring."""

    speed_clamped = _clamp(speed, -MAX_ARM_SPEED_DEG_S, MAX_ARM_SPEED_DEG_S)
    run_wheels(bot, speed_clamped, speed_clamped, duration_ms)
    wait(200)
    run_wheels(bot, -speed_clamped, -speed_clamped, duration_ms)

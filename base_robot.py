# base_robot.py

"""High-level helpers for LEGO SPIKE Prime missions using Pybricks.

Public method names stay the same so every mission file keeps working.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait


def _clamp(value, lower, upper):
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value


def _normalize_heading(angle):
    return (angle + 180) % 360 - 180

# ---------------------------------------------------------------------------
# Shared hub instance
# ---------------------------------------------------------------------------
# Creating the hub only once follows Pybricks guidance and prevents accidental
# SystemExit triggers caused by repeated PrimeHub() construction.
_HUB = PrimeHub()

# ---------------------------------------------------------------------------
# Hardware configuration
# ---------------------------------------------------------------------------
WHEEL_DIAMETER_MM = 62  # wheel outer diameter from the current build
AXLE_TRACK_MM = 140     # distance between wheel centres on the current build

# Motor ports (centralised so wiring changes are easy to audit).
LEFT_WHEEL_PORT = Port.F
RIGHT_WHEEL_PORT = Port.B
RIGHT_ARM_PORT = Port.A
LEFT_ARM_PORT = Port.E

# Drive motor directions. Left wheel is flipped relative to right so it uses
# COUNTERCLOCKWISE to ensure positive speeds move the robot forward.
LEFT_WHEEL_DIRECTION = Direction.COUNTERCLOCKWISE
RIGHT_WHEEL_DIRECTION = Direction.CLOCKWISE

# Arm gearing and direction (1.0 means motor degrees == arm degrees).
RIGHT_ARM_GEAR_RATIO = 1.0
LEFT_ARM_GEAR_RATIO = 1.0
RIGHT_ARM_DIRECTION = 1
LEFT_ARM_DIRECTION = 1

# Create motor objects once so ports are not claimed multiple times.
_LEFT_DRIVE_MOTOR = Motor(LEFT_WHEEL_PORT, LEFT_WHEEL_DIRECTION)
_RIGHT_DRIVE_MOTOR = Motor(RIGHT_WHEEL_PORT, RIGHT_WHEEL_DIRECTION)
_RIGHT_ARM_MOTOR = Motor(RIGHT_ARM_PORT)
_LEFT_ARM_MOTOR = Motor(LEFT_ARM_PORT)
_DRIVE_BASE = DriveBase(
    _LEFT_DRIVE_MOTOR,
    _RIGHT_DRIVE_MOTOR,
    wheel_diameter=WHEEL_DIAMETER_MM,
    axle_track=AXLE_TRACK_MM,
)

# Recommended speed limits taken from Pybricks docs (SPIKE Prime motors top out
# at roughly 1000 deg/s). Converted to mm/s for DriveBase usage.
MAX_DRIVE_SPEED_MM_S = 520   # ~1000 motor deg/s with 62 mm wheels
MAX_TURN_RATE_DEG_S = 400    # conservative turn rate to keep pivots stable
MAX_ARM_SPEED_DEG_S = 1000   # safe cap for attachment motors


class PybricksBot:
    """Facade over the SPIKE Prime hub, drive base, and attachments."""

    def __init__(self):
        self.hub = _HUB

        self.left_drive_motor = _LEFT_DRIVE_MOTOR
        self.right_drive_motor = _RIGHT_DRIVE_MOTOR
        self.drive_base = _DRIVE_BASE
        # Make sure previous missions are not holding the drive motors.
        self.drive_base.stop()
        self.drive_base.reset()

        self.right_arm_motor = _RIGHT_ARM_MOTOR
        self.left_arm_motor = _LEFT_ARM_MOTOR
        for m in (self.right_arm_motor, self.left_arm_motor):
            try:
                m.stop()
            except Exception:
                pass

        # Give missions a predictable heading baseline when the firmware supports it.
        try:
            self.hub.imu.reset_heading(0)
        except AttributeError:
            pass

    # ------------------------------------------------------------------
    # Driving helpers
    # ------------------------------------------------------------------

    def drive_forward(self, distance_cm, speed=200, gain=2.0):
        """Drive forward ``distance_cm`` centimetres while holding heading."""

        speed_mm_s = _clamp(speed, -MAX_DRIVE_SPEED_MM_S, MAX_DRIVE_SPEED_MM_S)
        target_heading = self.hub.imu.heading()
        target_distance_mm = max(0, distance_cm * 10)

        self.drive_base.reset()
        while self.drive_base.distance() < target_distance_mm:
            error = _normalize_heading(self.hub.imu.heading() - target_heading)
            correction = _clamp(-gain * error, -MAX_TURN_RATE_DEG_S, MAX_TURN_RATE_DEG_S)
            self.drive_base.drive(speed_mm_s, correction)
            wait(10)
        self.drive_base.stop()

    def drive_backward(self, distance_cm, speed=200, gain=2.0):
        """Drive backward ``distance_cm`` centimetres while holding heading."""

        speed_mm_s = _clamp(speed, -MAX_DRIVE_SPEED_MM_S, MAX_DRIVE_SPEED_MM_S)
        target_heading = self.hub.imu.heading()
        target_distance_mm = max(0, distance_cm * 10)

        self.drive_base.reset()
        while abs(self.drive_base.distance()) < target_distance_mm:
            error = _normalize_heading(self.hub.imu.heading() - target_heading)
            correction = _clamp(-gain * error, -MAX_TURN_RATE_DEG_S, MAX_TURN_RATE_DEG_S)
            self.drive_base.drive(-speed_mm_s, correction)
            wait(10)
        self.drive_base.stop()

    def turn_left(self, angle, speed=100):
        """Rotate left by ``angle`` degrees."""

        turn_rate = _clamp(speed, -MAX_TURN_RATE_DEG_S, MAX_TURN_RATE_DEG_S)
        start_heading = self.hub.imu.heading()
        self.drive_base.drive(0, -turn_rate)
        while abs(_normalize_heading(self.hub.imu.heading() - start_heading)) < angle:
            wait(10)
        self.drive_base.stop()
        wait(100)

    def turn_right(self, angle, speed=100):
        """Rotate right by ``angle`` degrees."""

        turn_rate = _clamp(speed, -MAX_TURN_RATE_DEG_S, MAX_TURN_RATE_DEG_S)
        start_heading = self.hub.imu.heading()
        self.drive_base.drive(0, turn_rate)
        while abs(_normalize_heading(self.hub.imu.heading() - start_heading)) < angle:
            wait(10)
        self.drive_base.stop()
        wait(100)

    # ------------------------------------------------------------------
    # Attachment helpers
    # ------------------------------------------------------------------

    def move_right_arm(self, degrees, speed=200):
        """Move the right attachment by motor ``degrees``."""

        speed_clamped = _clamp(speed, -MAX_ARM_SPEED_DEG_S, MAX_ARM_SPEED_DEG_S)
        self.right_arm_motor.run_angle(speed_clamped, degrees, then=Stop.HOLD, wait=True)

    def move_left_arm(self, degrees, speed=200):
        """Move the left attachment by motor ``degrees``."""

        speed_clamped = _clamp(speed, -MAX_ARM_SPEED_DEG_S, MAX_ARM_SPEED_DEG_S)
        self.left_arm_motor.run_angle(speed_clamped, degrees, then=Stop.HOLD, wait=True)

    # ------------------------------------------------------------------
    # Homing helpers
    # ------------------------------------------------------------------

    def home_right_arm(self, speed=80, timeout_ms=1500, direction=-1):
        """Home the right attachment to its mechanical stop and zero the angle."""

        speed_clamped = _clamp(speed, -MAX_ARM_SPEED_DEG_S, MAX_ARM_SPEED_DEG_S)
        run_until_stalled = getattr(self.right_arm_motor, "run_until_stalled", None)
        try:
            if callable(run_until_stalled):
                run_until_stalled(direction * speed_clamped, then=Stop.HOLD, timeout=timeout_ms)
            else:
                self.right_arm_motor.run(direction * speed_clamped)
                wait(timeout_ms)
                self.right_arm_motor.stop()
        finally:
            try:
                self.right_arm_motor.reset_angle(0)
            except AttributeError:
                pass

    def home_left_arm(self, speed=80, timeout_ms=1500, direction=1):
        """Home the left attachment to its mechanical stop and zero the angle."""

        speed_clamped = _clamp(speed, -MAX_ARM_SPEED_DEG_S, MAX_ARM_SPEED_DEG_S)
        run_until_stalled = getattr(self.left_arm_motor, "run_until_stalled", None)
        try:
            if callable(run_until_stalled):
                run_until_stalled(direction * speed_clamped, then=Stop.HOLD, timeout=timeout_ms)
            else:
                self.left_arm_motor.run(direction * speed_clamped)
                wait(timeout_ms)
                self.left_arm_motor.stop()
        finally:
            try:
                self.left_arm_motor.reset_angle(0)
            except AttributeError:
                pass

    def home_arms(self, right_speed=80, left_speed=80, timeout_ms=1500,
                  right_direction=-1, left_direction=1):
        """Home both attachments sequentially."""

        self.home_right_arm(speed=right_speed, timeout_ms=timeout_ms, direction=right_direction)
        wait(200)
        self.home_left_arm(speed=left_speed, timeout_ms=timeout_ms, direction=left_direction)

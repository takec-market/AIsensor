import math
import time

class FallDetector:
    """Simple fall detection using acceleration magnitude and orientation."""

    def __init__(self, acc_threshold=20.0, angle_threshold=60.0, time_threshold=1.0):
        self.acc_threshold = acc_threshold
        self.angle_threshold = angle_threshold
        self.time_threshold = time_threshold
        self._fall_start = None

    def update(self, ax, ay, az, timestamp=None):
        """Update the detector with new acceleration data.

        Parameters
        ----------
        ax, ay, az : float
            Acceleration values along each axis (m/s^2).
        timestamp : float, optional
            Time in seconds. If omitted, ``time.time()`` is used.

        Returns
        -------
        bool
            True if a fall is detected.
        """
        if timestamp is None:
            timestamp = time.time()

        magnitude = math.sqrt(ax * ax + ay * ay + az * az)
        if magnitude > self.acc_threshold:
            self._fall_start = timestamp

        if self._fall_start is not None:
            pitch = math.degrees(math.atan2(ax, az))
            if abs(pitch) > self.angle_threshold:
                if timestamp - self._fall_start >= self.time_threshold:
                    self._fall_start = None
                    return True
            else:
                # orientation recovered before time threshold
                self._fall_start = None
        return False

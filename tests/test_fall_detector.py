import os, sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from fall_detector import FallDetector


def test_detects_fall():
    detector = FallDetector(acc_threshold=20.0, angle_threshold=60.0, time_threshold=1.0)
    data = [
        (0.0, 0, 0, 9.81),
        (0.1, 21, 0, 9.81),
        (0.2, 9.81, 0, 0),
        (1.3, 9.81, 0, 0),
    ]
    detected = False
    for t, ax, ay, az in data:
        if detector.update(ax, ay, az, t):
            detected = True
    assert detected


def test_no_fall_when_orientation_recovers():
    detector = FallDetector(acc_threshold=20.0, angle_threshold=60.0, time_threshold=1.0)
    data = [
        (0.0, 0, 0, 9.81),
        (0.1, 21, 0, 9.81),
        (0.2, 0, 0, 9.81),
        (0.3, 0, 0, 9.81),
    ]
    for t, ax, ay, az in data:
        assert not detector.update(ax, ay, az, t)

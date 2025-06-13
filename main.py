import argparse
import csv
from fall_detector import FallDetector


def read_csv(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or row[0].startswith('#'):
                continue
            t, ax, ay, az = map(float, row)
            yield t, ax, ay, az


def main():
    parser = argparse.ArgumentParser(description="Simple fall detection demo")
    parser.add_argument("data", help="CSV file with timestamp, ax, ay, az")
    args = parser.parse_args()

    detector = FallDetector()
    for t, ax, ay, az in read_csv(args.data):
        if detector.update(ax, ay, az, t):
            print(f"FALL DETECTED at {t:.2f}s")


if __name__ == "__main__":
    main()

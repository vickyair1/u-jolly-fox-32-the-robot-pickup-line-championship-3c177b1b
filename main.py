"""Robot Pickup Line Championship entry.

Writes a single robot-themed pickup line to /output/entry.txt.
Standard library only, deterministic: same bytes on every run.
"""

import os

LINE = "Are you a software update? Because I never asked for you, but now I can't function without you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

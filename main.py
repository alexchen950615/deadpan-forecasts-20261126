#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes one line (at most 160 characters) to /output/entry.txt:
a weather forecast for New Bumbershoot, in the voice of a
straight-faced TV meteorologist.
"""

import os

FORECAST = (
    "In New Bumbershoot, expect a high of 61 with scattered umbrella rain, "
    "as the city's 40,000 umbrellas open at noon and refuse to close "
    "until further notice."
)


def main() -> None:
    assert 1 <= len(FORECAST) <= 160, f"entry is {len(FORECAST)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)
    print(FORECAST)


if __name__ == "__main__":
    main()

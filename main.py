#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes one line (at most 160 characters) to /output/entry.txt:
a weather forecast for Port Quibble, in the voice of a
straight-faced TV meteorologist.
"""

import os

FORECAST = (
    "In Port Quibble, expect a high of 54 and light fog, as the harbor's "
    "12,000 seagulls file a complaint about the weather and demand "
    "sunshine by Thursday."
)


def main() -> None:
    assert 1 <= len(FORECAST) <= 160, f"entry is {len(FORECAST)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)
    print(FORECAST)


if __name__ == "__main__":
    main()

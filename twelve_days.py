"""
Exercism solution for "twelve-days"
"""
from typing import List

DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

GIFTS = [
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
]

def recite(start: int, end: int) -> List[str]:
    """
    Recite The Twelve Days of Christmas from the start to the end verse.
    """
    result = []
    for day in range(start - 1, end):
        nth = DAYS[day]
        gifts_and = " "
        if day > 0:
            gifts_and += ", ".join(GIFTS[len(GIFTS) - day:]) + ", and "
        result.append(
            f"On the {nth} day of Christmas my true love gave to me:" \
            f"{gifts_and}a Partridge in a Pear Tree.")
    return result
from typing import Literal

Rotation = Literal['L', 'R']

def parse_rotation(value: str) -> Rotation:
    value = value[0]
    rotation = value[:1]
    number = int(value[1:])
    if rotation == 'L':
        return number * -1
    elif rotation == 'R':
        return number
    else:
        raise ValueError(f"Invalid rotation: {rotation}")

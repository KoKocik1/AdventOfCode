def parse_rotation(value: str) -> int:
    rotation = value[0]
    number = int(value[1:])
    if rotation == 'L':
        return -number
    elif rotation == 'R':
        return number
    else:
        raise ValueError(f"Invalid rotation: {rotation}")

def check_zero_end(act_value: int, rotation: int, password: int) -> tuple[int, int]:
    """Check if we hit 0 after rotation."""
    act_value = (act_value + rotation) % 100
    if act_value == 0:
        password += 1
    return act_value, password


def check_zero(act_value: int, rotation: int, password: int) -> tuple[int, int]:
    """Check if we hit 0 during rotation (excluding starting position) by iterating step-by-step."""
    if rotation == 0:
        return act_value, password
    
    step = -1 if rotation < 0 else 1
    for _ in range(abs(rotation)):
        act_value = (act_value + step) % 100
        if act_value == 0:
            password += 1
    return act_value, password


def check_zero_math(act_value: int, rotation: int, password: int) -> tuple[int, int]:
    """Check if we hit 0 during rotation using optimized math approach."""
    if rotation == 0:
        return act_value, password

    full_hundreds = abs(rotation) // 100
    if full_hundreds > 0:
        password += full_hundreds
    
    remainder = (abs(rotation) % 100) * (1 if rotation > 0 else -1)
    act_value, password = check_zero(act_value, remainder, password)
    
    return act_value, password

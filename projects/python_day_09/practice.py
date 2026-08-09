def check_dlc(dlc):
    """Return dlc if it is a valid CAN DLC (0-8), else raise ValueError."""
    if not (0 <= dlc <= 8):
        raise ValueError(f"dlc must be 0-8, got {dlc}")
    return dlc

print(check_dlc(4))
check_dlc(9)
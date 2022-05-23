def validate_pin(pin):
    return True if len(pin) in (4, 6) and pin.isdigit() == True else False

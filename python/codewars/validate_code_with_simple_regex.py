def validate_code(code):
    return True if str(code)[:1] in ("1","2","3") else False
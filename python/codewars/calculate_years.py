def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        principal = principal + (principal * interest) - (principal * interest * tax)
        y += 1
    return y

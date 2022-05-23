number = 17

def print_formatted(number):
    spacer = len(str(format(number, 'b'))) +1
    for i in range(1, int(number+1)):
        a = i
        b = format(i, 'o')
        c = format(i, 'X')
        d = format(i, 'b')
        
        print(f"{' ' * (spacer-1-len(str(a)))}{a}{' ' * (spacer-len(str(b)))}{b}{' ' * (spacer-len(str(c)))}{c}{' ' * (spacer-len(str(d)))}{d}")

print_formatted(number)    

# ax*x+bx+c

def ecf():
    a = float(input('fist'))
    b = float(input('second'))
    c = float(input('third'))
    x = float(input('four'))
    if a == 0:
        if b == 0:
            sum = c
        else:
            sum = b*x+c
    else:
        if b == 0:
            sum = a*x*x+c
        else:
            sum = a*x*x+b*x+c

    print(sum)


ecf()

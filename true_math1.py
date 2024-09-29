from math import inf

def divide(first, second):
    if second == 0:
        print(inf)
    else:
        if type(first) == int and type(second) == int:
            print(first / second)
            return

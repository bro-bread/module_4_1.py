def divide(first, second):
    if second == 0:
        print('Ошибка')
    else:
        if type(first) == int and type(second) == int:
            print(first / second)
            return


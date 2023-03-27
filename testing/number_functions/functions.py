import warnings

def is_even(number):
    number = float(number)
    
    # print(number, number - int(number))

    if number - int(number) != 0:
        warnings.warn("Got number with decimal part: {}".format(number))
        number = int(number)

    if number % 2 == 0:
        return True
    else:
        return False
from typing import Union, List
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


def geo_mean(numbers: List[Union[int, float]]) -> float:
    numbers = list(numbers) # I wanna raise a TypeError if not convertable
    n = len(numbers)

    product = 1
    for number in numbers:
        if type(number) not in (int, float):
            raise(TypeError(f"Expecting int or float, got {type(number)}"))
        if number < 0:
            raise(ValueError(f"Got invalid input: {number}"))

        product *= number

    return round(pow(product, 1/n), 4)


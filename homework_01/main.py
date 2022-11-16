"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num):
    return [num ** 2 for num in num]


    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(p_int: int) -> bool:
    flag = 0
    if p_int < 2:
        return False
    for i in range(2, (p_int // 2) + 1):
        if p_int % i == 0:
            flag = 1
            break

    return flag == 0


def filter_numbers(p_list: list, p_type_item: str) -> list:
    if p_type_item == ODD:
        return list(filter(lambda x: x % 2 != 0, p_list))
    elif p_type_item == EVEN:
        return list(filter(lambda x: x % 2 == 0, p_list))
    elif p_type_item == PRIME:
        return list(filter(is_prime, p_list))
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
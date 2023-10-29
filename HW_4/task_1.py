# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). 
# Можете использовать любую парадигму, но рекомендую использовать функциональную, 
# т.к. в этом примере она значительно упростит вам жизнь.


from functools import reduce
import math


def Pearson_correlation(array_1, array_2):
    if len(array_1) != len(array_2) or len(array_1) == 0 or len(array_2) == 0:
        return None

    average_value_x = sum(array_1) / len(array_1)
    average_value_y = sum(array_2) / len(array_2)

    # Числитель
    r_numerator = reduce(
        lambda x, y: x + y,
        map(lambda x: (x[0] - average_value_x) * (x[1] - average_value_y),
            zip(array_1, array_2)))

    sum_x = reduce(lambda x, y: x + y,
                   map(lambda x: (x - average_value_x)**2, array_1))
    sum_y = reduce(lambda x, y: x + y,
                   map(lambda y: (y - average_value_y)**2, array_2))

    # Знаменатель
    r_denominator = math.sqrt(sum_x * sum_y)
    if r_denominator == 0:
        return None
    return r_numerator / r_denominator


print(Pearson_correlation([4, 2, 3], [1, 5, 6]))


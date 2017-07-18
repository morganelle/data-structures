"""Python implemementation of a radix sort algorithm for integers."""


def radix_sort(unsorted_list, set_digit=0):
    """Return sorted list of integers using radix sort algorithm."""
    if type(unsorted_list) not in [list, tuple] or len(unsorted_list) < 1:
        raise TypeError('Please enter a list or a tuple with at least one value.')
    unsorted_list = list(unsorted_list)
    num_list = [list() for _ in range(10)]
    sorted_list = []
    sort_complete = True
    for item in unsorted_list:
        _verify_input(item)
        digit = _get_digit(item, set_digit)
        if item >= 10 ** (set_digit + 1):
            sort_complete = False
        num_list[digit].append(item)
    for i in range(10):
        for item in num_list[i]:
            sorted_list.append(item)
    if sort_complete:
        return sorted_list
    return radix_sort(sorted_list, set_digit=set_digit + 1)


def _get_digit(number, place):
    """Identify target place for a number."""
    return ((number // 10 ** place) % 10)


def _verify_input(input_item):
    """Validate input items."""
    if type(input_item) is not int:
        raise TypeError('{} is not an integer'.format(input_item))
    if input_item < 0:
        raise ValueError('{} is not a positive integer'.format(input_item))


if __name__ == '__main__':  # pragma no cover
    from timeit import Timer
    best_case_short = Timer(
        'radix_sort([x for x in range(10)])',
        'from __main__ import radix_sort'
    )
    best_case_long = Timer(
        'radix_sort([x for x in range(100)])',
        'from __main__ import radix_sort'
    )
    worst_case_short = Timer(
        'radix_sort([x for x in range(10)][::-1])',
        'from __main__ import radix_sort'
    )
    worst_case_long = Timer(
        'radix_sort([x for x in range(100)][::-1])',
        'from __main__ import radix_sort'
    )
    random_short = Timer(
        'radix_sort([randint(0, 10) for x in range(10)])',
        'from __main__ import radix_sort; from random import randint'
    )
    random_long = Timer(
        'radix_sort([randint(0, 1000) for x in range(100)])',
        'from __main__ import radix_sort; from random import randint'
    )
    random_long_dupes = Timer(
        'radix_sort([randint(0, 2) for x in range(1000)])',
        'from __main__ import radix_sort; from random import randint'
    )
    print('''
    Here are some results for several test cases for the quick sort,
    run 100 times each:

    Best case for 10 numbers: {} seconds
    Best case for 1000 numbers: {} seconds

    Worst case for 10 numbers: {} seconds
    Worst base for 1000 numbers: {} seconds

    Random case for 10 numbers: {} seconds
    Random case for 1000 numbers: {} seconds
    Random case for 1000 numbers with lots of duplicates
    (secretly, the real worst case): {} seconds
    '''.format(best_case_short.timeit(100),
               best_case_long.timeit(100),
               worst_case_short.timeit(100),
               worst_case_long.timeit(100),
               random_short.timeit(100),
               random_long.timeit(100),
               random_long_dupes.timeit(100)))

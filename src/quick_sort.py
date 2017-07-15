"""Python implemementation of a quick sort algorithm."""


def quick_sort(unsorted_list):
    """Sort values with quick sort algorithm."""
    if type(unsorted_list) not in [list, tuple] or len(unsorted_list) < 1:
        raise TypeError('Please enter a list or a tuple with at least one value.')
    unsorted_list = list(unsorted_list)
    pivot = unsorted_list[0]
    _verify_input(pivot)
    sorted_list = []
    list1 = []
    list2 = []
    for i in range(1, len(unsorted_list)):
        _verify_input(unsorted_list[i])
        if unsorted_list[i] < pivot:
            list1.append(unsorted_list[i])
        else:
            list2.append(unsorted_list[i])
    if len(list1) >= 2:
        list1 = quick_sort(list1)
    if len(list2) >= 2:
        list2 = quick_sort(list2)
    sorted_list += list1
    sorted_list.append(pivot)
    sorted_list += list2
    return sorted_list


def _verify_input(input_item):
    """Validate input items."""
    if type(input_item) not in [int, float]:
        raise TypeError('{} is not a numeric value'.format(input_item))


if __name__ == '__main__':  # pragma no cover
    from timeit import Timer
    best_case_short = Timer(
        'quick_sort([x for x in range(10)])',
        'from __main__ import quick_sort'
    )
    best_case_long = Timer(
        'quick_sort([x for x in range(100)])',
        'from __main__ import quick_sort'
    )
    worst_case_short = Timer(
        'quick_sort([x for x in range(10)][::-1])',
        'from __main__ import quick_sort'
    )
    worst_case_long = Timer(
        'quick_sort([x for x in range(100)][::-1])',
        'from __main__ import quick_sort'
    )
    random_short = Timer(
        'quick_sort([randint(0, 10) for x in range(10)])',
        'from __main__ import quick_sort; from random import randint'
    )
    random_long = Timer(
        'quick_sort([randint(0, 1000) for x in range(100)])',
        'from __main__ import quick_sort; from random import randint'
    )
    random_long_dupes = Timer(
        'quick_sort([randint(0, 2) for x in range(1000)])',
        'from __main__ import quick_sort; from random import randint'
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

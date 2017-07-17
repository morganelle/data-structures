"""Python implementation of a Insertion Sort."""


def insertion_sort(iter_item):
    """Perform a insertion sort on an iterable."""
    if type(iter_item) not in [list, tuple]:
        raise TypeError('Please enter a list or tuple.')
    sort_list = list(iter_item)
    if type(sort_list[0]) not in [float, int]:
        raise TypeError('This bubble sort handles integers and floats only.')
    for x in range(len(sort_list) - 1):
        if type(sort_list[x + 1]) not in [float, int]:
                raise TypeError('This bubble sort handles integers and floats only.')
        if sort_list[x] > sort_list[x + 1]:
            sort_list[x], sort_list[x + 1] = sort_list[x + 1], sort_list[x]
            for y in range(x, 0, -1):
                if sort_list[y] < sort_list[y - 1]:
                    sort_list[y], sort_list[y - 1] = sort_list[y - 1], sort_list[y]
                else:
                    break
    return sort_list


if __name__ == '__main__':  # pragma no cover
    from timeit import Timer
    best_case_short = Timer(
        'insertion_sort([x for x in range(10)])',
        'from __main__ import insertion_sort'
    )
    best_case_long = Timer(
        'insertion_sort([x for x in range(100)])',
        'from __main__ import insertion_sort'
    )
    worst_case_short = Timer(
        'insertion_sort([x for x in range(10)][::-1])',
        'from __main__ import insertion_sort'
    )
    worst_case_long = Timer(
        'insertion_sort([x for x in range(100)][::-1])',
        'from __main__ import insertion_sort'
    )
    random_short = Timer(
        'insertion_sort([randint(0, 1000) for x in range(10)])',
        'from __main__ import insertion_sort; from random import randint'
    )
    random_long = Timer(
        'insertion_sort([randint(0, 1000) for x in range(100)])',
        'from __main__ import insertion_sort; from random import randint'
    )
    random_long_dupes = Timer(
        'insertion_sort([randint(0, 2) for x in range(1000)])',
        'from __main__ import insertion_sort; from random import randint'
    )
    print('''
    Here are some results for several test cases for the bubble sort,
    run 100 times each:

    Best case for 10 numbers: {} seconds
    Best case for 1000 numbers: {} seconds

    Worst case for 10 numbers: {} seconds
    Worst base for 1000 numbers: {} seconds

    Random case for 10 numbers: {} seconds
    Random case for 1000 numbers: {} seconds
    Random case for 1000 numbers with lots of duplicates
    (secretly, the real worst case): {} seconds
    '''.format(best_case_short.timeit(100), best_case_long.timeit(100), worst_case_short.timeit(100), worst_case_long.timeit(100), random_short.timeit(100), random_long.timeit(100), random_long_dupes.timeit(100)))

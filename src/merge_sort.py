def merge_sort(new_list):
    """sorts a list through merge sort methods"""
    if type(new_list) not in [list, tuple]:
        raise TypeError('must pass in a list or a tuple')
    new_list = list(new_list)
    sorted_list = list_split(new_list)
    return sorted_list


def list_split(new_list):
    """splits the list until it has 1 element"""
    if len(new_list) < 2:
        if type(new_list[0]) not in [int, float]:
            raise TypeError('the list must only have numbers')
        return new_list
    halfpt = len(new_list) // 2
    list1 = list_split(new_list[:halfpt])
    list2 = list_split(new_list[halfpt:])
    sorted_list = sort_list(list1, list2)
    return sorted_list


def sort_list(list1, list2):
    """sorts the list"""
    index1 = 0
    index2 = 0
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    sorted_list = []
    while True:
        if type(list1[index1]) not in [int, float] or type(list2[index2]) not in [int, float]:
            raise TypeError('the list must only have numbers')
        if list1[index1] > list2[index2]:
            sorted_list.append(list2[index2])
            index2 += 1
        else:
            sorted_list.append(list1[index1])
            index1 += 1
        if index1 == len(list1):
            sorted_list += list2[index2:]
            return sorted_list
        if index2 == len(list2):
            sorted_list += list1[index1:]
            return sorted_list


if __name__ == '__main__':  # pragma no cover
    from timeit import Timer
    best_case_short = Timer(
        'merge_sort([x for x in range(10)])',
        'from __main__ import merge_sort'
    )
    best_case_long = Timer(
        'merge_sort([x for x in range(100)])',
        'from __main__ import merge_sort'
    )
    worst_case_short = Timer(
        'merge_sort([x for x in range(10)][::-1])',
        'from __main__ import merge_sort'
    )
    worst_case_long = Timer(
        'merge_sort([x for x in range(100)][::-1])',
        'from __main__ import merge_sort'
    )
    random_short = Timer(
        'merge_sort([randint(0, 1000) for x in range(10)])',
        'from __main__ import merge_sort; from random import randint'
    )
    random_long = Timer(
        'merge_sort([randint(0, 1000) for x in range(100)])',
        'from __main__ import merge_sort; from random import randint'
    )
    random_long_dupes = Timer(
        'merge_sort([randint(0, 2) for x in range(1000)])',
        'from __main__ import merge_sort; from random import randint'
    )
print('''
Here are some results for several test cases for the merge sort,
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

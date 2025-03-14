from typing import List

# def pair_sum_unsorted_array(numbers, target):
#   hMap = {}

#   for i, n in enumerate(numbers):
#     diff = target - n

#     if diff in hMap:
#       return [hMap[diff], i]
    
#     hMap[n] = i

#   return
    
# numbers = [2, 1, 5, 3]
# target = 4
# print(pair_sum_unsorted_array(numbers, target))


def two_sum(numbers:List[int], target: int):
    hMap = {}
    for i, n in enumerate(numbers):
        diff = target - n

        if diff in hMap:
            return [hMap[diff], i]
        hMap[n] = i

    return [-1, -1]

numbers = [5, 3, 10, 45, 1]
target = 6

print(two_sum(numbers, target))

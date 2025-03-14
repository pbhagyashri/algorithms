def intersection_of_three_sorted_arrays(arr1, arr2, arr3):
    p1 = 0
    p2 = 0
    p3 = 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):

        if arr1[p1] == arr2[p2] == arr3[p3]:
          result.append(arr1[p1])

        minimum = min(arr1[p1], arr2[p2], arr3[p3])

        if arr1[p1] == minimum:
          p1 += 1

        if arr2[p2] == minimum:
          p2 += 1

        if arr3[p3] == minimum:
          p3 += 1
    
    if len(result) == 0:
      result.append(-1)
    return result

arr1 = [1, 2, 2, 2, 9]
arr2 = [1, 1, 2, 2]
arr3 = [1, 1, 1, 2, 2, 2]

print(intersection_of_three_sorted_arrays(arr1, arr2, arr3))
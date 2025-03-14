def pair_sum_sorted_array(numbers, target):
    for n in numbers:
        l = 0
        r = len(numbers) - 1
        match = target - n

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l, r]
            
            if sum > target:
                r -= 1
            else:
                l += 1

numbers = [1, 2, 3, 5, 10]
target = 7
print(pair_sum_sorted_array(numbers, target))
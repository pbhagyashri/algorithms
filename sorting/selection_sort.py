# brut force algorithm with quadratic O(n**2) time complexity
def selection_sort(arr):
    if len(arr) <= 1:
        return arr
        
    for i in range(0, len(arr)):
        # record current minimum
        curr_min_index = i
        
        # start the second iteration from i+1 to length of the array
        for j in range(i + 1, len(arr)):
            # see if any of the numbers in the array starting from index i+1 is smaller that current minimun at index i
            if(arr[j] < arr[curr_min_index]):
                # if new minimum is found, replace it's index with current minimum index
                curr_min_index = j
                
        # swap the current minimum with new minimum
        arr[i], arr[curr_min_index] = arr[curr_min_index], arr[i]
        
    return arr

arr = [5, 8, 3, 9, 4, 1, 7]
selection_sort(arr)

print(arr)
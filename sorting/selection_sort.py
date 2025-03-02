# def selection_sort(arr):
#   if len(arr) <= 1:
#     return arr
  
#   for i in range(0, len(arr)):
#     curr_min_index = i
#     temp = arr[i]
#     for j in range(i + 1, len(arr) - 1):
#       if arr[j] < arr[curr_min_index]:
#         curr_min_index = j

#     arr[i] = arr[curr_min_index]
#     arr[curr_min_index] = temp

def selection_sort(arr):
    if len(arr) <= 1:
        return arr
        
    for i in range(0, len(arr)):
        curr_min_index = i
        temp = arr[i]
        
        for j in range(i + 1, len(arr)):
            if(arr[j] < arr[curr_min_index]):
                curr_min_index = j

        arr[i] = arr[curr_min_index]
        arr[curr_min_index] = temp
        
    return arr

arr = [5, 8, 3, 9, 4, 1, 7]
selection_sort(arr)

print(arr)
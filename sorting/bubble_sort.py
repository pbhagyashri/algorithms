# brut force algorithm with quadratic O(n**2) time complexity
def bubble_sort(arr):
  # start the outer for loop from right to left decresing the index by 1
  for i in range(len(arr) - 1, 0, -1):
    # start another inner for loop from index i to 0. (i + 1 ensures we don't run into out of bound index)
    for j in range(i + 1, 0, -1):
      # create 2 pointers, 
      # right pointer, r points to right most element at index i arr[i]
      # left pointer, l points to the element left to right most element, j - 1
      r = i
      l = j - 1 # (j - 1 ensures we don't run into out of bound index)

      # if element on the right is smaller than the element on left, swap the 2 elements
      # bubbling up the smallest element to start of the array
      if(arr[r] < arr[l]):
        arr[l], arr[r] = arr[r], arr[l]

arr = [1, 9, 2, 0, 3, 7, 1]
bubble_sort(arr)

print('arr', arr)
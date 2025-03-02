def bubble_sort(arr):
  for i in range(len(arr) - 1, 0, -1):
    
    for j in range(i + 1, 0, -1):
      r = i
      l = j - 1

      if(arr[r] < arr[l]):
        arr[l], arr[r] = arr[r], arr[l]

arr = [1,9,2,0,3,7, 1]
bubble_sort(arr)

print('arr', arr)
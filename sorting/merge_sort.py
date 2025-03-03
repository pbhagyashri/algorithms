def merge(arr, start, end):
  # base case
  if(start == end):
    return arr
  
  # calulate mid point
  mid = (start + end) // 2
  # recursively call the merge function on the left half
  merge(arr, start, mid)
  # recursively call the merge function on the right half
  merge(arr, mid+1, end)

  i = start
  j = mid + 1
  aux = []

  while i <= mid and j <= end:
    print('i:', i, j)
    if arr[i] <= arr[j]:
      aux.append(arr[i])
      i += 1
    else:
      aux.append(arr[j])
      j += 1
  while i <= mid:
    aux.append(arr[i])
    i += 1
  while j <= end:
    aux.append(arr[j])
    j += 1

  arr[start:end+1] = aux

def merge_sort(arr):
  merge(arr, 0, len(arr) - 1)
  return arr

arr = [5, 8, 3, 9, 4, 1, 7]
merge_sort(arr)
print(arr)
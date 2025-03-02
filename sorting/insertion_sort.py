def insertion_sort(a):
  for i in range(1, len(a)):
    # store ith element in the array in a temporary veriable
    temp = a[i]
    # store the element before it in another variable, j
    j = i - 1

    # if j is greater or equal to 0, do the folowoing steps
    # first iteration - 
    # j = 0 and i = 1.
    # 8 is the temp value and a[j] = 5 which is smaller that 8 so we never hit the while loop
    # second iteration -
    # i = 2, j = 1, a[i], temp = 3. a[j] = 8 which is bigger than temp so we shift everything ot right
    # decrease j by 1 and repeat the steps. 3 is smaller than 5 so we shift again
    # exit the loop, at this point we have [3,5,8,9,4,1,7]
    # we continue to process for the rest of the array
    while j >= 0 and a[j] > temp:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = temp
  return a

arr = [5, 8, 3, 9, 4, 1, 7]
print(insertion_sort(arr))

# best case time complexity - O(n)
# worst case time complexity - O(n**2)
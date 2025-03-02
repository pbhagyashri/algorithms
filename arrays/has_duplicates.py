def has_duplicates(arr):
  hashset = set()

  for a in arr:
    if a in hashset:
      return True
    hashset.add(a)
  return False

arr = [1, 2, 3, 3]
print(has_duplicates(arr))
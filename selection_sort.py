def selection_sort(arr):
  for i in range (len(arr)):
    minimal_index = i
    for j in range(i+1, len(arr)):
      if arr[minimal_index]>arr[j]
        minimal_index = j
    arr[i], arr[minimal_index] = arr[minimal_index], arr[i]

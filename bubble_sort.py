def bubble_sort(arr):
  for i in range(len(arr)):
    swap = False
    for i in range(0, len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swap = True
    if swap is False:
      break

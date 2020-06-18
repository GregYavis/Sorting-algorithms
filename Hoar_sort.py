def quick_sort(arr):
  if len(arr)<=1:
    return
  else:
    barrier = arr[0]
    L = []
    R = []
    M = []
    for i in arr:
      if i < barrier:
        L.append(i)
      elif i == barrier:
        M.append(i)
      else:
        R.append(i)
    quick_sort(L)
    quick_sort(R)
    i = 0
    for digit in L+M+R:
      arr[i] = digit
      i += 1

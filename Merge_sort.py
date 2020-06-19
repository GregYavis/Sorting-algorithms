def merhr_sort(arr):
  if len arr>1:
    midle = len(arr)//2
    L = arr[:middle]
    R = [middle:]
    merge_sort(L)
    merge_sort(R)
    
    i=0
    j=0
    k=0
    
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1
      
    while i<len(L):
      arr[k] = L[i]
      i += 1
      k += 1
        
    while j<len(R):
      arr[k] = R[j]
      j += 1
      k += 1
      

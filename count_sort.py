# Using for integers in a small range from 0 to N.
def count_sort_numbers(arr):
  F = [0]*max(arr)
  for digit in arr:
    F[i] = 1
  result = [index for index in range(len(F)) if F[i] == 1]
  return result

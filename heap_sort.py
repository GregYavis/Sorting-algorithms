def heapify(arr, n, i):
  l = 2*i+1
  r = 2*i+2
  largest = i
  
    """
    [12, 11, 13, 1, 6, 7, 4, 0, 3, 8]
    [0,   1,  2, 3, 4, 5, 6, 7, 8, 9]
        К примеру берём третий индекс, для которого дочерние индексы: левый = 7, правый = 8.
    принимаем третий индекс, как индекс по которому располагается самое большое из 
    сравниваемых чисел.
        1 не менше чем 0, следовательно пока по этому индексу действительно 
    находится самое большое число и мы переходим к сравнению с правым 
    дочерним элементом.
        1 меньше 3, следовательно мы принимаем индекс по которому 
    располагается 3 как индекс содержащий самое большое число.
        Далее сравниваем индекс largest и индекс с которым производилось 
    изначальное сравнение, если изначально взятые дочерние елементы 
    оказались меньше, то мы не изменяли максимальный индекс и изменений не 
    требуется. Если же один из элементов оказался больше, то largest != i
    и мы меняем эти елементы местами.    
    """
  
  if l < n and arr[i] < arr[l]:
    largest = l
  if r < n and arr[largest] < arr[r]:
    largest = r
    
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)
    
def heap_sort(arr):
  n = len(arr)
  """ Вычисления производятся для половины массиваа в обратном порядке, 
    так как все индексы на дочерние елементы можно получить обработав уже 
    только эту половину
    """
  for i in range(n // 2-1, -1, -1):
    heapifr(arr, n, i)
     """
    В результате предыдущих операций получаем кучу вида:
    [13, 11, 12, 3, 8, 7, 4, 0, 1, 6]
    В которой дочерние елементы меньше родительских, но ещё не являются 
    полностью отсортированными.
     """
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[1]
    heapift(arr, i, 0)
  print(arr)
  

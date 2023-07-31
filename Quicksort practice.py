def partition(array, low, high):
             pivot = array[high]
             i = low - 1
             j = low
             while j <= high:
                if array[j]<=pivot:
                    i+=1
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
                j+=1
             return i
         
def QuickSort(array, low, high):
    if high <= low:
          return
    pivot = partition(array, low, high)
    QuickSort(array, low, pivot-1)
    QuickSort(array, pivot+1, high)
    return array

array = [8,2,4,7,1,3,9,6,5]

QuickSort(array, 0, len(array)-1)

print(array)
import random
import sys
import time
import gc

#def ProgrammingAssignment1():
#function to swap integers
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

#function to compute the median of 3 numbers
def medianof3(a,b,c):
    if (a < b and b < c) or (c < b and b < a):
        return b
    elif (b < a and a < c) or (c < a and a < b):
        return a
    else:
        return c
    
#check if the array is sorted or not
def isSorted(arr,n):
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            return False
    return True

#function to generate a sorted array of size n.
def sortedArray(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr

#function to generate aan array of size n filled with constants.
def constArray(n):
    arr = []
    for i in range(n):
        arr.append(0)
    return arr

#function to generate a random array of size n.
def randomArray(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,1000))
    return arr

#function to implement selection sort. 
#input: data - array to be sorted, n - number of elements in the array
#output: sorted array (ascending order)
def selectionSort(data,n):
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = swap(data[i], data[min])
    return data

#helper function for merge sort
def mergeFn(data, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    leftArr = []
    rightArr = []
    
    for i in range(n1):
        leftArr.append(data[left + i])
    for j in range(n2):
        rightArr.append(data[mid + 1 + j])

    i = 0
    j = 0

    k = left
    while i < n1 and j < n2:
        if leftArr[i]<= rightArr[j]:
            data[k] = leftArr[i]
            i += 1
        else:
            data[k] = rightArr[j]
            j += 1
        
        k += 1

    while i < n1:
        data[k] = leftArr[i]
        i += 1
        k += 1

    while j < n2:
        data[k] = rightArr[j]
        j += 1
        k += 1

    return data

#function to implement merge sort
#input: data - array to sort, n - number of elements in array
#output: sorted array (ascending order)
def mergeSort(data,left,right):
    if left< right:
        mid = (left + right) // 2
        data = mergeSort(data,left,mid)
        data = mergeSort(data,mid+1,right)

        data = mergeFn(data,left,mid,right)

    return data

#helper function for quick sort
def partition(data, low, high):
    x = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= x:
            i += 1
            data[i], data[j] = swap(data[i], data[j])
    data[i+1], data[high] = swap(data[i+1], data[high])
    return i+1

#function to implement quick sort
#input: data - array to sort, n - number of elements in array
#output: sorted array (ascending order)
def quickSort(data, low, high):
    if (low < high):
        q = partition(data, low, high)
        quickSort(data, low, q-1)
        quickSort(data, q+1, high)
    return data

#function to implement insertion sort
#input: data - array to sort, n - number of elements in array
#output: sorted array (ascending order)
def insertionSort(data, n):
    for i in range(1,n):
        key = data[i]
        #insert data[i] into the sorted subarray data[1:i-1]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -=1
        data[j+1] = key
    return data


#main function. input arguments:
#type of array to generate - 'r' - random, 's' - sorted,'c' - constant
#side of array to evaluate on - any positive integer > 0
#sorting algorithm to evaluate - 'q' - quicksort, 'i' - insertion sort, 'm' - merge sort, 's' - selection sort
#output: time taken to run sorting algorithm 
arrayType = "r"
n = 10
algo = "q"

if len(sys.argv) != 4:
    print("Invalid command line arguments. Using defaults. Running quick sort on a random array of length 10")
else:
    try:
        arrayType = sys.argv[1]
        n = int(sys.argv[2])
        algo = sys.argv[3]
    except:
        print("Invalid command line arguments. Using defaults. Running quick sort on a random array of length 10")
        arrayType = "r"
        n = 10
        algo = "q"
    if arrayType not in ['r','s','c']:
        print(f"Invalid array type. Using default ranadom array of length {n}")
        arrayType = "r"
    if algo not in ['q','i','m','s']:
        print(f"Invalid sorting algorithm. Using default Quick Sort")
        algo = "q"
    if n <= 0:
        print(f"Number of elements in array must be positive and greater than 0. Using default length {n}")
        n = 10
print(f"Array type: {arrayType} Array length: {n}, Algo: {algo}")

data = []
output = []

for i in range(3):
    if arrayType == "r":
        data = randomArray(n)
    elif arrayType == "s":
        data = sortedArray(n)
    elif arrayType == "c":
        data = constArray(n)

startTime = 0
endTime = 0
totalTime = [0] * n
success = False

match algo:
    case "q":
        for i in range(3):
            gc.collect() #garbage collection 
            startTime = time.perf_counter()
            output = quickSort(data,0,n-1)
            endTime = time.perf_counter()
            totalTime[i] = endTime - startTime
            success = isSorted(output,n)
    case "s":
        for i in range(3):
            gc.collect() #garbage collection 
            startTime = time.perf_counter()
            output = selectionSort(data,n)
            endTime = time.perf_counter()
            totalTime[i] = endTime - startTime
            success = isSorted(output,n)
    case "i":
        for i in range(3):
            gc.collect() #garbage collection 
            startTime = time.perf_counter()
            output = insertionSort(data,n)
            endTime = time.perf_counter()
            totalTime[i] = endTime - startTime
            success = isSorted(output,n)
    case "m":
        for i in range(3):
            gc.collect() #garbage collection 
            startTime = time.perf_counter()
            output = mergeSort(data,0,n-1)
            endTime = time.perf_counter()
            totalTime[i] = endTime - startTime
            success = isSorted(output,n)

if not success:
    print("Your sorting algorithm failed multiple runs. Aborting...")
    for i in range(len(output)):
        print(output[i])
else:
    print("Median Execution time: " + str(medianof3(totalTime[0],totalTime[1],totalTime[2])))
    #for i in range(n):
        #print(output[i])

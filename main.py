import multiprocessing as mp
import random
import time
import numpy as np

def shuffleFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    random.shuffle(lines)

    with open(filename, 'w') as file:
        file.writelines(lines)

# Function to find the partition position
def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)

if __name__ == '__main__':
    file = "names.txt"
    array = []
    # Read the file and store to an array
    with open(file, 'r') as file:
        array = file.readlines()
    
    #Sort the array and record time, This is withouth parallel processing
    arr1 = 
    start = time.time()
    quickSort(array, 0, len(array)-1)
    end = time.time()
    print(f"Runtime: {end - start:.6f} seconds")
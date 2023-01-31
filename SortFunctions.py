####################################
# Quick Sort Algorithm taken from:
# url https://tutorialedge.net/compsci/sorting/quicksort-in-python/
# on 01/25/2023
# Selection Sort Algorithm taken from:
# url https://big-o.io/algorithms/comparison/selection-sort/
# on 01/25/2023
# Change log
# -quick sort pivot value change to the array middle index
####################################

def quicksort(array):
    ## We define our 3 arrays
    less = []
    equal = []
    greater = []

    ## if the length of our array is greater than 1
    ## we perform a sort
    if len(array) > 1:
        ## Select our pivot. This doesn't have to be
        ## the first element of our array
        pivot = array[int(len(array)/2)]

        ## recursively go through every element
        ## of the array passed in and sort appropriately
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        ## recursively call quicksort on gradually smaller and smaller
        ## arrays until we have a sorted list.
        return quicksort(less) + equal + quicksort(greater)

    else:
        return array

    # end def quicksort(array):

def selection_sort(array):
    currentIndex = 0
    while currentIndex < len(array) - 1:
        minIndex = currentIndex
        i = currentIndex + 1
        while i < len(array):
            if (array[minIndex] > array[i]):
                minIndex = i
            i += 1
        if (minIndex != currentIndex):
            temp = array[minIndex]
            array[minIndex] = array[currentIndex]
            array[currentIndex] = temp
        currentIndex += 1

# end def selection_sort(array):


if __name__ == "__main__":
    print(quicksort([6, 4, 7, 1, 2, 3, 9, 12, 3]))


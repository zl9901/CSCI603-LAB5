"""
CSCI-603: Wk 7 Sorting
Author: Sean Strout @ RIT CS

Implementations of in-place sorts for selectionSort and
mergeSort.
"""
import random
import time
# test case data
def generate_data(N):
    result=list(range(N))
    random.shuffle(result)
    return result
arr=[]
brr=[]
DATA1 =generate_data(10000)


def get(Index):
    sum = 0
    arr.append(Index)
    for i in range(len(arr)):
        sum=sum+arr[i]
    brr.append(sum)

def _findMinIndex(data, mark):
    """
    A helper routine for selectionSort which finds the index
    of the smallest value in data at the mark index or greater.
    :param data: a list of data
    :param mark: an index which is in range 0..len(data)-1 inclusive
    :return: An index which is in range 0..len(data)-1 inclusive
    """

    # assume the minimum value is at initial mark position
    minIndex = mark
    count=0

    # loop over the remaining positions greater than the mark
    for mark in range(mark+1, len(data)):
        # if a smaller value is found, record its index
        count+=1
        if data[mark] < data[minIndex]:
            minIndex = mark

    return minIndex,count

def selectionSort(data):
    """
    Perform an in-place selection sort of data.
    :param data: The data to be sorted (a list)
    :return: None
    """
    newcount=0
    for mark in range(len(data)-1):
        minIndex,count = _findMinIndex(data, mark)
        newcount=newcount+count
        # swap the element at marker with the min index
        data[mark], data[minIndex] = data[minIndex], data[mark]
    return newcount



def _split(data):
    """
    Split the data into halves and return the two halves
    :param data: The list to split in half
    :return: Two lists, cut in half
    """
    return data[:len(data)//2], data[len(data)//2:]

def _merge(left, right):
    """
    Merges two sorted list, left and right, into a combined sorted result
    :param left: A sorted list
    :param right: A sorted list
    :return: One combined sorted list
    """

    # the sorted left + right will be stored in result
    result = []
    leftIndex, rightIndex = 0, 0

    # loop through until either the left or right list is exhausted
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    Index=leftIndex+rightIndex
    get(Index)

    # take the un-exhausted list and extend the remainder onto the result
    if leftIndex < len(left):
        result.extend(left[leftIndex:])
    elif rightIndex < len(right):
        result.extend(right[rightIndex:])

    return result

def mergeSort(data):
    """
    Performs a merge sort and returns a newly sorted list.
    :param data: A list of data
    :return: A sorted list
    merge[0]的结果是[0],而merge[5,0]的结果才是[0,5]
    merge函数得出的结果返回给了mergeSort函数
    """

    # an empty list, or list of 1 element is already sorted
    if len(data) < 2:
        return data
    else:
        # split the data into left and right halves
        left, right = _split(data)

        # return the merged recursive mergeSort of the halves
        return _merge(mergeSort(left), mergeSort(right))


def testSelectionSort():
    """
    A test function for the selection sort.
    :return: None
    """
    print('Seletion Sort\t\t100\t\t',end='')
    start=time.time()
    count = selectionSort(DATA1)
    end=time.time()
    print(count, "\t\t",end-start)
def testMergeSort():
    """
    A test function for merge sort.
    :return: None
    """

    print('Merge Sort\t\t100\t\t', end='')
    startnew=time.time()
    mergeSort(DATA1)
    endnew = time.time()
    print(brr[-1], "\t\t", endnew-startnew)
    #print(brr[-1])
    #print(arr)
    #print(brr)

def main():
    """
    Main function.
    :return: None
    """
    print("ALGORITHM\t\tN\t\tCOMPARISONS\t\tSECONDS")
    testSelectionSort()
    testMergeSort()
if __name__ == '__main__':
    main()
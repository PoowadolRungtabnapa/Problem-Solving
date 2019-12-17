def quickSort(data_list) :
    quickSortHlp(data_list, 0 ,len(data_list) - 1)

def quickSortHlp(data_list,first,last) :
    if first < last :

        splitpoint = partition(data_list, first, last)

        quickSortHlp(data_list, first, splitpoint - 1)
        quickSortHlp(data_list,splitpoint+1,last)

def partition(data_list,first,last) :
    pivotvalue = data_list[first + 1]

    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
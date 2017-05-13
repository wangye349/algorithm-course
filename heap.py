def build_max_heap(array):
    n = len(array)
    for i in range(int(n/2)):
        array = max_heapify(array,int(n/2)-1-i)

    return array

def max_heapify(array, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if(l <= len(array) - 1) and (array[l] > array[i]):
        largest = l
    else:
        largest = i

    if(r <= len(array) - 1) and (array[r] > array[largest]):
        largest = r

    if(largest != i):
        temp = array[largest]
        array[largest] = array[i]
        array[i] = temp
        array = max_heapify(array,largest)

    return array






    # if(2*i+3 < len(array)):
    #     if(array[2*i+1] < array[2*i+2]):
    #         if(array[2*i+2] > array[i]):
    #             temp = array[i]
    #             array[i] = array[2*i+2]
    #             array[2*i+2] = temp
    #     else:
    #         if(array[2*i+1] > array[i]):
    #             temp = array[2*i+1]
    #             array[2*i+1] = array[i]
    #             array[i] = temp
    # else:
    #     if(array[2*i+1] > array[i]):
    #         temp = array[2*i+1]
    #         array[i] = array[2*i+1]
    #         array[2*i+1] = temp
    #
    # return array

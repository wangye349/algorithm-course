import heap
import read_test_files
import time
import math

string = read_test_files.read_test_files1("test_hundred_thousands.txt")

array = string[1:len(string)-1]

#this is the sort function
time1 = time.time()
new_array1 = array[:]

new_array1.sort()

# for i in range(len(new_array1)/2):
#     temp = new_array1[len(new_array1)-i-1]
#     new_array1[len(new_array1)-i-1] = new_array1[i]
#     new_array1[i] = temp

print new_array1[:100]

time2 = time.time()

print "this is the sort function time:", time2 - time1

#this is heapsort
time1 = time.time()

new_array2 = array[:]
new_array2 = heap.build_max_heap(new_array2)

array_been_heapsort = []
for i in range(len(new_array2)):
    temp = new_array2[len(new_array2)-1]
    new_array2[len(new_array2)-1] = new_array2[0]
    new_array2[0] = temp
    array_been_heapsort.append(new_array2[len(new_array2)-1])
    del new_array2[len(new_array2)-1]
    heap.max_heapify(new_array2,0)

# for i in range(len(array_been_heapsort)/2):
#     temp = array_been_heapsort[len(array_been_heapsort)-i-1]
#     array_been_heapsort[len(array_been_heapsort)-i-1] = array_been_heapsort[i]
#     array_been_heapsort[i] = temp

time2 = time.time()
print array_been_heapsort[:100]
print "this is the heapsort time", time2 - time1

import read_test_files
import time
import math

string = read_test_files.read_test_files1("test_hundred_thousands.txt")

numble = string[1:len(string)-1]

#this is insertion sort
# time1 = time.time()
# new_numbles1 = numble[:]
# for i in range(1,len(new_numbles1)):
#     i_point = new_numbles1[i]
#     for j in range(1,i + 1):
#         if(new_numbles1[i - j] >= i_point):
#             new_numbles1[i - j + 1] = new_numbles1[i - j]
#             new_numbles1[i - j] = i_point
#         else:
#             break
#
# time2 = time.time()
# print new_numbles1[:100]
# print "this is the insertion sort running time",time2 - time1
#
# #this is binary_research sort
#
# time1 = time.time()
# import binary_research
#
# new_numbles = numble[:]
#
# if(new_numbles[0] > new_numbles[1]):
#     temp = new_numbles[1]
#     new_numbles[1] = new_numbles[0]
#     new_numbles[0] = temp
#
# for i in range(2,len(new_numbles)):
#     i_point = new_numbles[i]
#     place = binary_research.binary_research(new_numbles[:i],i_point)
#     for j in range(0,i-int(place)):
#         new_numbles[i - j] = new_numbles[i - j - 1]
#     new_numbles[place] = i_point
#
# print new_numbles[:100]
# time2 = time.time()
# print "this is the binary research sort time",time2 - time1

#this is the merge sort
time1 = time.time()

new_numbles3 = numble[:]

def compare_two(numbles_in):
    if(numbles_in[0] > numbles_in[1]):
        temp = numbles_in[0]
        numbles_in[0] = numbles_in[1]
        numbles_in[1] = temp
        return numbles_in
    else:
        return numbles_in

def compare_two_strings(numbles_in1, numbles_in2):
    numbles_out = []
    pointer1 = 0
    pointer2 = 0
    for i in range(len(numbles_in1) + len(numbles_in2)):
        if(numbles_in1[pointer1] < numbles_in2[pointer2]):
            numbles_out.append(numbles_in1[pointer1])
            pointer1 = pointer1 + 1
            if(pointer1 == len(numbles_in1)):
                numbles_out.extend(numbles_in2[pointer2:])
                break
        else:
            numbles_out.append(numbles_in2[pointer2])
            pointer2 = pointer2 + 1
            if(pointer2 == len(numbles_in2)):
                numbles_out.extend(numbles_in1[pointer1:])
                break
    return numbles_out

# a = [3,1]
# l = len(a)
# nl = a[:int(l/2)]
# nr = a[int(l/2):]
#
# print compare_two_strings(nl, nr)
# print "******(*&*&(*(*&(*&))))"
def merge_sort(numbels):
    numbels_left = numbels[:int(len(numbels)/2)]
    numbels_right = numbels[int(len(numbels)/2):]
    if(len(numbels) == 1):
        return numbels
    else:
        return compare_two_strings(merge_sort(numbels_left),merge_sort(numbels_right))

print merge_sort(new_numbles3)[:100]

#def merge_sort_two(numbels):










# numbles_l = divided_left(new_numbles3)
# numbles_r = divided_right(new_numbles3)
#
# numbles_l = divided_left(numbles_l)
# numbles_r = divided_right(numbles_r)
#
# if(len(numbles_l) < 2):
#     return compare_two(numbles_l)
# else:
#     return compare_two_strings(numbles_l,numbles_r)
#
# while True:
#     if(len(numbles_l) == 2):
#         numbles_l = compare_two(numbles_l)
#         numbles_r = compare_two(numbles_r)
#         break
#     else:
#         numbles_l = divided_left(numbles_l)
#         numbles_r = divided_right(numbles_r)
#
# while True:
#     if(len(numbles_r) == 0.5 * len(new_numbles3)):
#         break
#     else:
#         numbles_l = compare_two_strings(numbles_l,numbles_r)
#
# numbles_l = divided_left(new_numbles3)
# numbles_r = divided_right(new_numbles3)
#
# signs = 0
# def merge_sort(numbles):
#     if(signs == 0):
#         numbles_l = divided_left(numbles_l)
#         numbles_r = divided_right(numbles_r)
#
#
#
# numbles_l =
#
#
#
# def divided_right(numbles_in):
#     return numbles_in[:len(numbles_in)/2]
#
# def divided_left(numbles_in):
#     return numbles_in[len(numbles_in)/2:]
#

time2 = time.time()
print "this is the running time of merge sort: ", time2 - time1


#this is the sort function
time1 = time.time()
new_numbles4 = numble[:]

new_numbles4.sort()

print new_numbles4[:100]
time2 = time.time()

print "this is the sort function time:", time2 - time1

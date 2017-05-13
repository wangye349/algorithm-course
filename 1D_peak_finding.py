import time
import math
import read_test_files
string = read_test_files.read_test_files1("test.txt")


# f = open("test.txt","r")
# string = f.read().split(" ")
# del string[len(string)-1]
# string_clone = string[:]
# string.append(0)
# for i in range(len(string)-1):
#     string[i+1] = int(string_clone[i])
# f.close()
# string[0] = 0
# string.append(0)


#this is the normal version
time1 = time.time()
for i in range(1,len(string)-1):
    if(string[i] >= string[i-1]) & (string[i] >= string[i+1]):
        b = string[i]
        break
print b
time2 = time.time()
time_runs = time2 - time1
print time_runs

print "this is to print the maxma in the string"
print "**************"
time1 = time.time()
print max(string)
time2 = time.time()
print time2 - time1
print "***************"

print "****************"
time1 = time.time()
m = string[0]
for i in range(len(string)):
    if (string[i] > m):
        m = string[i]
print m
time2 = time.time()
print time2 - time1
print "***********"
#this is the peak finding version
time1 = time.time()
def oneD_peak(string_input):
    for i in range(int(math.log(len(string_input),2))+10):
        if(string_input[int(len(string_input)/2)] < string_input[int(len(string_input)/2) + 1]):
            string_input = half_string(string_input,1)
            #oneD_peak(string_input[int(len(string_input)/2):])
        elif(string_input[int(len(string_input)/2)] < string_input[int(len(string_input)/2) - 1]):
            string_input = half_string(string_input,0)
            #oneD_peak(string_input[:int(len(string_input)/2)])
        else:
            return string_input[int(len(string_input)/2)]
            break

def half_string(string_input1,first_or_last):
    if(first_or_last == 1):
        return string_input1[int(len(string_input1)/2):]
    elif(first_or_last == 0):
        return string_input1[:int(len(string_input1)/2)]
    else:
        return 0


print oneD_peak(string)
time2 = time.time()
print time2 - time1

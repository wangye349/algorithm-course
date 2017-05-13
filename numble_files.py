import random
f = open("test_for_sort.txt","w")
for i in range(1,10000):
    f.write(str(10000 - i))
    f.write(" ")
f.close()









# f = open("test_small.txt","r")
# string = f.read()
# string_split = string.split(" ")
# print string_split
# print len(string_split)
# del string_split[len(string_split) - 1]
# print len(string_split)
# print "***************"
# print string_split[0]
# print string_split[1]
# print string_split[len(string_split)]
# numble = []
# for i in range(0,len(string_split)):
#     #numble.append(int(string_split[i]))
#     string_split[i] = int(string_split[i])
#     print string_split[i]
#     #print numble[i], "\n"
# f.close

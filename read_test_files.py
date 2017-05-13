def read_test_files1(file_name):
    f = open(file_name,"r")
    string = f.read().split(" ")
    del string[len(string)-1]
    string_clone = string[:]
    string.append(0)
    for i in range(len(string)-1):
        string[i+1] = int(string_clone[i])
    f.close()
    string[0] = 0
    string.append(0)
    return string

from random import randint
import time


def time_it(func):
    def time_of_it(*args, **keyargs):
        time1 = time.time()
        _result = func(*args, **keyargs)
        time2 = time.time()
        print(time2 - time1)
        return _result
    return time_of_it


# @time_it
def merge_sort(input_to_sort_list):
    # left = input_to_sort_list[: int(len(input_to_sort_list) / 2)]
    # right = input_to_sort_list[int(len(input_to_sort_list) / 2):]
    a = []
    if len(input_to_sort_list) > 1:
        left = merge_sort(input_to_sort_list[: int(len(input_to_sort_list) / 2)])
        right = merge_sort(input_to_sort_list[int(len(input_to_sort_list) / 2):])
        input_to_sort_list = left + right
        j = int(len(input_to_sort_list) / 2)
        i = 0
        while i < int(len(input_to_sort_list) / 2)\
                and j < len(input_to_sort_list):
            if input_to_sort_list[i] <= input_to_sort_list[j]:
                a.append(input_to_sort_list[i])
                i += 1
            else:
                a.append(input_to_sort_list[j])
                j += 1
        else:
            a = a + input_to_sort_list[i : int(len(input_to_sort_list) / 2)]
            a = a + input_to_sort_list[j : len(input_to_sort_list)]
        return a
    else:
        return input_to_sort_list
        # if input_to_sort_list[0] <= input_to_sort_list[1]:
        #     a.append(input_to_sort_list[0])
        #     a.append(input_to_sort_list[1])
        # else:
        #     a.append(input_to_sort_list[1])
        #     a.append(input_to_sort_list[0])
        # return a


def test_sorted(test_input_list):
    for i in range(len(test_input_list) - 1):
        if test_input_list[i] > test_input_list[i + 1]:
            return False
    else:
        return True


def main():
    to_sort_list = [randint(1, 100000) for _ in range(10000)]
    time1 = time.time()
    sorted_list = merge_sort(to_sort_list)
    time2 = time.time()
    print(time2 - time1)
    # print(sorted_list)
    print(test_sorted(sorted_list))


if __name__ == "__main__":
    main()










    # a = []

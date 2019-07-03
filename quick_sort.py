from random import randint, shuffle
import time


def partition(input_list, lo, hi):
    if hi - lo == 2:
        if input_list[lo] <= input_list[hi - 1]:
            return lo
        else:
            input_list[lo], input_list[hi - 1] = input_list[hi - 1], input_list[lo]
            return hi - 1
    v = input_list[lo]
    i = lo + 1
    j = hi - 1
    while i < j:
        while input_list[i] <= v and i < hi - 1:
            i += 1
        while input_list[j] >= v and j > lo:
            j -= 1
        if j > i:
            input_list[i], input_list[j] = input_list[j], input_list[i]
    if i == j:
        input_list[lo], input_list[i] = input_list[i], input_list[lo]
        return i
    else:
        input_list[lo], input_list[i - 1] = input_list[i - 1], input_list[lo]
        return i - 1


def quick_sort(input_list, lo, hi):

    if(hi - lo > 1):
        partition_index = partition(input_list, lo, hi)
        quick_sort(input_list, lo, partition_index)
        quick_sort(input_list, partition_index + 1, hi)
    else:
        return input_list


def test_sorted(test_input_list):
    for i in range(len(test_input_list) - 1):
        if test_input_list[i] > test_input_list[i + 1]:
            return False
    else:
        return True


def main(n):
    average = []
    for i in range(n):
        list_to_sort = [randint(1,10000000) for _ in range(10000)]
        time1 = time.time()
        shuffle(list_to_sort)
        quick_sort(list_to_sort, 0, len(list_to_sort))
        time2 = time.time()
        average.append(time2 - time1)
        if not test_sorted(list_to_sort):
            print('there is a false sort')
    print(sum(average) / len(average))
    # print(time2 - time1)
    # print(list_to_sort)
    # print(test_sorted(list_to_sort))


if __name__ == "__main__":
    main(1000)


# if __name__ == "__main__":
#     # a = list(range(8))input_list[lo], input_list[i - 1] = input_list[i - 1], input_list[lo]
#     # shuffle(a)
#     a = [8, 7, 6, 5, 4, 3, 2, 1]
#     a = [1, 2, 3, 7, 5, 6, 7, 8]
#     partition_index = partition(a, 0, 2)
#     pass

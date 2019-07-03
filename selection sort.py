from random import randint


def min_index_of_list(input_list_to_min):
    min_index = 0
    for i in range(len(input_list_to_min)):
        if input_list_to_min[i] < input_list_to_min[min_index]:
            min_index = i
    return min_index


def sort_list(input_list):
    for i in range(len(input_list)):
        rest_list = input_list[i:]
        min_index = i + min_index_of_list(rest_list)
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list


def test_sorted(test_input_list):
    for i in range(len(test_input_list) - 1):
        if test_input_list[i] > test_input_list[i + 1]:
            return False
    else:
        return True


def main():
    to_sort_list = [randint(1,1000) for _ in range(500)]
    sorted_list = sort_list(to_sort_list)
    print(sorted_list)
    print(test_sorted(sorted_list))


if __name__ == "__main__":
    main()

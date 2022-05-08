import timeit

def bubble_sort_1(list_of_numbers):  # 4n^2 - 8n + 5 -> O(n^2)
    number_of_elements = len(list_of_numbers)  # 1
    for i in range(number_of_elements - 1):  # n - 1, (n - 1) * (4n - 4) = 4n^2 - 4n - 4n +4= 4n^2 - 8n + 4
        for j in range(number_of_elements - 1):  # n - 1, (n - 1) * 4 = 4n - 4
            if list_of_numbers[j] > list_of_numbers[j + 1]:  # 1 , 4 * 1 = 4
                temp = list_of_numbers[j]  # 1
                list_of_numbers[j] = list_of_numbers[j + 1]  # 1
                list_of_numbers[j + 1] = temp  # 1

def bubble_sort_2(list_of_numbers):
    number_of_elements = len(list_of_numbers)
    end_index = number_of_elements - 1
    for i in range(number_of_elements - 1):
        for j in range(end_index):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                temp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = temp
        end_index -= 1

def bubble_sort_3(list_of_numbers):
    number_of_elements = len(list_of_numbers)
    end_index = number_of_elements - 1
    for i in range(number_of_elements - 1):
        was_change = False
        for j in range(end_index):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                temp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = temp
                was_change = True
        if not was_change:
            break
        end_index -= 1

def bubble_sort_4(list_of_numbers):
    number_of_elements = len(list_of_numbers)
    end_index = number_of_elements - 1
    start_index = 0
    for i in range(number_of_elements - 1):
        was_change = False
        for j in range(start_index, end_index):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                temp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = temp
                if not was_change:
                    if j > 0:
                        start_index = j - 1
                was_change = True
        if not was_change:
            break
        end_index -= 1

def execution_time(sorting_function, data_size, number_of_tests):
    test_code = f'sorting_function(list_to_sort)'
    print(timeit.timeit(stmt=test_code,
                        globals={'sorting_function': sorting_function,
                                 'list_to_sort': list_of_numbers},
                        number=number_of_tests))

list_of_numbers = [5, 3, 8, 10, 0, 6, 4, -1, 56, 7, -85, 24, -2, 9]

if __name__ == '__main__':
    data_size = len(list_of_numbers)
    number_of_tests = 1000
    print("bubble_sort_1:")
    execution_time(bubble_sort_1, data_size, number_of_tests)
    print("bubble_sort_2:")
    execution_time(bubble_sort_2, data_size, number_of_tests)
    print("bubble_sort_3:")
    execution_time(bubble_sort_3, data_size, number_of_tests)
    print("bubble_sort_4:")
    execution_time(bubble_sort_4, data_size, number_of_tests)
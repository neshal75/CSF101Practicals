# linear search
def linear_s(classroom, student):
    for i in range(len(classroom)):
        if classroom[i] == student:
            return i
    return -1
test_list = ["dorji", "pema", "janu", "raju"]
result = linear_s(test_list,"dorji")
print(f"linear search: the in index of dorji is {result}")


# binary search
def binary_search(numbers, wanted):
    left,right = 0, len(numbers) -1
    while left <= right:
        mid = (left + right)//2
        if numbers[mid] == wanted:
            return mid
        elif numbers[mid] < wanted:
            left =  mid + 1
        else:
            right =  mid - 1
    return -1
list_numbers = [1,7,3,5]
list_number_sorted = [1,3,5,7]
list_number_sorted = sorted(list_numbers)
final_result = binary_search(list_number_sorted,5)
print(f"Binary search: the binary search of the 5 is {final_result}")


# compare performance between linear and binary
import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low,high = 0, len(arr) -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def compare_search_algorithms(arr, target):
    # linear search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time

    # Binary Search
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time

    print(f"Linear Search: found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: found at index {binary_result}, Time: {binary_time:.6f} seconds")
large_list = list(range(100000))
compare_search_algorithms(large_list, 77777)

# binary search recursive
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, mid - 1, left)
test_list_sorted = [1,2,3,4,5,6]
result = binary_search_recursive(test_list_sorted, 5, 0, len(test_list_sorted) -1)
print(f"recursive binary search: index of 5 in sorted list is {result}")





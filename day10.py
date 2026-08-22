# Day 10 of python problem solving

# 1. find second largest number
def find_second_largest_number(list:list):
    largest:int = list[0]
    second_largest:int = list[0]
    
    for i in list:
        if i>largest:
            second_largest = largest
            largest = i
        elif( i > second_largest and i != largest):
            second_largest = i
    print(second_largest)
find_second_largest_number([1,2,3,4,100,12])





## bubble sort algorithm
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not efficient for large data sets as its average and worst-case time complexity are quite high.


def bubble_sort(arr: list):
    n: int = len(arr)

    for i in range(0, n - 1):
        swapped: bool = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    print(arr)


# bubble_sort([64, 34, 25, 12, 22, 11, 90])




# 2. Find Missing Number
# find_missing([1, 2, 3, 5, 6])
# Output: 4
def find_missing(list:list):
    missing_list:list = []
    bubble_sort(list)
    for i in range(0, len(list)-1):
        if( list[i+1] - list[i] > 1):
            missing_list.append(list[i]+1)
    print(missing_list)

find_missing([1, 2, 3, 5, 6])

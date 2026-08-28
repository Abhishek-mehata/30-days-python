
# 2. phase 1
# def bubble_sort(list:list):
#     size = len(list)
    
#     for i in range(0, size-1):
#         for j in range(0, size-1):
#             # for j in range
#             if list[j] > list[j+1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp
#     return list;

# if __name__ == "__main__":
#     elements = [5,9,2,1,67,34,88,34]
#     bubble_sort(elements)
#     print(elements)


# phase 2
# def bubble_sort(list:list):
#     size = len(list)

#     for i in range(0, size-1):
#         for j in range(0, size-i-1):
#             # for j in range
#             if list[j] > list[j+1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp
#     return list;

# if __name__ == "__main__":
#     # elements = [5,9,2,1,67,34,88,34]
#     elements = [1,2,3]
#     bubble_sort(elements)
#     print(elements)



# phase 3
def bubble_sort(list:list):
    size = len(list)
    swapped = False;

    for i in range(0, size-1):
        for j in range(0, size-i-1):
            # for j in range
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                swapped = True
        if not swapped:
            break;
    return list;

if __name__ == "__main__":
    # elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3]
    bubble_sort(elements)
    print(elements)

# day 9 of python problem solving series

# 1. remove duplicates from a list
def remove_duplicates(list:list):
    duplicates:dict = {}
    new_list:list = []
    
    for i in list:
        if i in duplicates:
            duplicates[i] = duplicates[i] + 1;
        else:
            duplicates[i] = 1
    
    for key in duplicates:
        new_list.append(key)
    print(new_list)
remove_duplicates([1,1,2,2,3])


# 2. find the missing number
def find_missing(list:list):
    missingList:list = []
    
    for i in range( len(list) - 1 ):
        if list[i + 1] - list[i] > 1:
            missingList.append(list[i] + 1)
    print(missingList)
find_missing([1, 2, 3, 5, 6])
        

    
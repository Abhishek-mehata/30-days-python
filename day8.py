# day 8 of python problem solving

# 1. frequency of a number in a list
# Given a list of integers and a number x, count how many times x appears in the list.
def frequency_in_list(list:list, target:int):
    count:int = 0
    
    for i in list:
        if(i == target):
            count = count + 1;
    print(count)
frequency_in_list([2, 5, 2, 8, 2, 9, 5], 9);



# 2. remove duplicates
# given a list of numbers, task is to remove the duplicates and form a new list
def remove_duplicates(list:list):
    newList:list = []
    duplicate:dict = {}
    for i in list:
        if i in duplicate:
            duplicate[i] = duplicate[i] + 1
        else:
            duplicate[i] = 1
    for key in duplicate:
        newList.append(key)
    print(newList)
remove_duplicates([11,11,2,4,4,5,6,6])





# 3. find non repeating element in a list
def non_repeating_element(list:list):
    duplicate:dist = {}
    non_repeating_list:list = []
    
    for i in list:
        if i in duplicate:
            duplicate[i] = duplicate[i] + 1
        else:
            duplicate[i] = 1
    
    for key in duplicate:
        if(duplicate[key] == 1):
            non_repeating_list.append(key);
    print(non_repeating_list)
non_repeating_element([1,2,2,3,5,3,5])
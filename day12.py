# day 11 of python problem solving

# count the occurence of each element of array
def count_occurence(arr:list):
    count_dist:dict = {}
    
    for i in arr:
        if i in count_dist:
            count_dist[i] = count_dist[i] + 1
        else:
            count_dist[i] = 1
    
    # traverse through the dictionary
    for key in count_dist:
        print(f"{key}   ->   {count_dist[key]}")
# count_occurence([1, 2, 2, 3, 1, 4, 2, 3])


# find the first non-repeating number in an array
def find_non_repeating(arr:list):
    first_occuring:int 
    data_dictionary:dict = {}
    
    for i in arr:
        if i in data_dictionary:
            data_dictionary[i] = data_dictionary[i] + 1
        else:
            data_dictionary[i] = 1
    
    # traversing through the dictionary
    for key in data_dictionary:
        if(data_dictionary[key] == 1):
            # print(data_dictionary[key])
            first_occuring = data_dictionary[key]
    print(first_occuring)
find_non_repeating([4, 5, 1, 2, 1, 4, 5])
# Day 7 python series

# find second largest number in a list
def second_largest(list:list):
    if(len(list) < 2):
        print("The expection operation is not possible for given data")
        return;
    
    lrg_num:int = list[1];
    scnd_lrg_num:int =list[2];
    
    
    for item in list:
        if(item>lrg_num):
            scnd_lrg_num = lrg_num
            lrg_num = item
        elif item > scnd_lrg_num and item != lrg_num:
            scnd_lrg_num = item
    print(scnd_lrg_num)
second_largest([1,4,12,7,22,23,44,35])


# character frequency counter

def frequency_counter(text:str):
    data:dict = {};
    
    for char in text:
        if char in data:
            data[char] +=   1
        else:
            data[char] = 1
    print(data)
frequency_counter("apple")
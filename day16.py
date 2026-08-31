# day 16 of python problems solving

# 2. Find the First Non-Repeating Element
def find_first_non_repeating(arr:list):
    arrLength:int = len(arr);
    data:dict = {};
    firstNonRepeating:int = 0
    
    for i in arr:
        if i in data:
            data[i] = data[i] + 1
        else: 
            data[i] = 1
    
    for key in data:
        if data[key] == 1:
            firstNonRepeating = key;
            print(f"The first non repeating element is {key}");
            return;
find_first_non_repeating([4, 5, 1, 2, 1, 4, 5])


# 2. Move All Zeros to the End
def move_zeros(arr:list):
    newArr:list = []
    for i in arr:
        if i != 0:
            newArr.append(i)
    
    for j in arr:
        if j == 0:
            newArr.append(j)
    print(newArr)
move_zeros([0, 1, 0, 3, 12])
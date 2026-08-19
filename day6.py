# Day 6 of python problem solving


# prime number
def prime_checker(num:int):
    if(num == 1):
        print("not a prime number")
        return;
    temp:int = num
    is_prime:bool = True
    
    for i in range(2, int(num/2) + 1):
        if(num%i == 0):
            is_prime=False
            break
    
    if(is_prime):
        print("It is a prime number")
    else:
        print("It is not a prime number")
prime_checker(3)

# find the largest digit
def find_largest_digit(num:int):
    arr:list = [];
    temp:int = num;
    
    while temp>0:
        digit = temp % 10;
        arr.append(digit);
        temp = temp // 10
    # print(arr)
    
    largest:int = arr[0]
    for i in arr:
        if(i>largest):
            largest = i
    print(f"The largest digit is {largest}")
find_largest_digit(5832)
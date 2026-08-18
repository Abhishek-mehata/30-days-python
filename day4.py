# Day4 of python problem solving

# 1. sum of even numbers
# n=10
# 2 + 4 + 6 + 8 + 10 = 30
def sum_of_even_numbers(n:int):
    sum:int = 0    
    # if(n%2 != 0):
    #     n = n + 1;

    for i in range(2, n+1):
        if i%2 == 0:
            sum = sum + i
    print(sum);

sum_of_even_numbers(10);


# 2. count no. of even and odd numbers
# n=10
# Even: 5
# Odd: 5

def count_even_odd(n):
    even_count:int = 0
    odd_count:int = 0
    
    for i in range(1,n+1):
        if i%2 ==0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    print(f"Even Count: {even_count}\nOdd Count: {odd_count}");
count_even_odd(10);


# 3. find the larget number in a list of numbers
def find_largest(list:list):
    largest:int  = list[0];
    
    for i in list:
        if(i>largest):
            largest = i
    print(largest)

find_largest([12,45,7,89,23])


# 4. Count digits of a given number
def count_digits(num:int):
    temp:int = num
    count:int = 0
    
    while temp>0:
        temp = temp // 10;
        count = count + 1;
    print(count)
count_digits(58392)

# 5. reverse a number
def reverse_number(num:int):
    temp:int = num
    reversed_number:int = 0
    digit:int =0
    
    while temp>0:
        digit = temp % 10
        reversed_number = digit+(reversed_number*10)
        temp = temp // 10
    print(reversed_number)
reverse_number(123)
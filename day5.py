# Day 5 of python program solving

# 1. Factorial of a number
def factorial(num:int):
    fact:int = 1;
    temp:int = num;
    
    while temp > 0:
        fact = fact * temp
        temp = temp - 1
    print(fact)
factorial(5)


# 2. count vowels in given string
def count_vowels(string:str):
    vowels:list = ['a','e','i','o','u']
    vowels_count:int = 0
    data:str = string.lower()
    
    for i in data:
        for j in vowels:
            if(i == j):
                vowels_count = vowels_count + 1
    print(vowels_count)
count_vowels("Hello World")

# 3. sum of digits of a number
def sum_of_digits(num:int):
    sum:int = 0;
    temp:int = num;
    
    while temp > 0:
        digit = temp % 10;
        sum = sum + digit;
        temp = temp // 10
    print(sum)
sum_of_digits(12345)


# 4. prime checker
def check_prime(num:int):
    temp:int = num
    is_prime:bool = True
    
    if(num <= 1):
        print("Not prime")
        return;

    for i in range(2, int(num/2)):
        if(num % i == 0):
            is_prime = False
    
    if(is_prime):
        print("It's a prime number")
    else:
        print("It's not a prime number")
check_prime(14)


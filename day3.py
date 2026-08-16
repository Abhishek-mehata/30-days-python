# day 3 of 30 days problem solving

# 1. sum of n natural numbers
def sum_of_natural_numbers(n:int):
    sum=int(0)
    
    for i in range(1, n+1):
        sum  = sum + i
    
    print(f"The sum of given {n} natural numbers is {sum} ");

# sum_of_natural_numbers(5);

# 2. count digits of a given number
def count_digits(num:int):
    temp:int = num
    count=int(0)
    
    while temp>0:
        temp = temp // 10;
        count = count + 1
    
    print(f"Given number {num} has {count} digits");

# count_digits(4455)

# 3. Revrse a given number
def reverse_number(num:int):
    reverse:int = 0
    digit:int
    temp:int = num
    
    while temp>0:
        digit = temp%10;
        reverse = digit + (reverse*10)
        temp = temp//10
    
    print(f"The reverse of {num} is {reverse}")
# reverse_number(9878)


# 4. Palindrome checker
# Check whether a number reads the same forward and backward
def check_palindrome(num:int):
    temp:int = num
    reverse:int = 0
    digit:int
    
    while temp>0:
        digit = temp % 10;
        reverse = digit + (reverse*10);
        temp = temp//10;
    
    if num == reverse:
        print(f"{num} is a palindrome number")
    else:
        print(f"{num} is not a palindrome number")
# check_palindrome(111)


# 5. Factorial of a number
# 5! = factorial of 5 = 5x4x3x2x1
def factorial(num:int):
    fact:int = 1
    
    if num == 0:
        print("0")
        return;
    
    for i in range(1,num+1):
        fact = fact*i;
    print(f"The factorial of {num} is {fact}")
# factorial(5)


# 6. Check weather given number is prime of not
def check_prime(num:int):
    isPalindrome:bool = True;
    
    if num<=1:
        print("Not prime")
        return;

    for i in range(2, int(num/2 + 1)):
        if(num%i == 0):
            isPalindrome = False
            break
    
    if isPalindrome:
        print(f"The number {num} is a prime number")
    else:
        print(f"The number {num} is not a prime")
check_prime(7)
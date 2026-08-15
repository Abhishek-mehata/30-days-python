# Day 2

# 1. print numbers from 1 to 10
# or natural numbers from 1 to n

def print_natural_numbers(n):
    for i in range(1,n+1):
        print(i)
print_natural_numbers(10)


# 2. Multiplication Table
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
# multiplication_table(7);


# 3. obtain no of digits in given number
def count_digits(num):
    temp = int(num)
    count=int(0)
    
    while temp>0:
        temp=temp // 10
        count=count+1
    
    print(count)

# 15 / 4 -> Float Division -> 3.75
# 15 // 4 -> Floor Division -> 3
# 15 % 4 -> Remainder -> 3
# count_digits(58392)


# 4. Reverse a number
def reverse_number(num):
    temp = int(num)
    reverse = int(0)
    
    
    while temp>0:
        digit = temp%10 # 123 % 10 => 3
        reverse = digit + (reverse*10) # 3 + (reversex10)
        temp = temp//10
    print(reverse)

# reverse_number(12345)


# 5. Prime number
# prime number is a number that is only divisible by 1 and itself like 5,7,13
def check_prime(num):
    if(num<=1):
        print("Not Prime")
        return
    
    is_prime = bool(True)
    
    for i in range(2, int(num/2 +1) ):
        if num%i==0:
            is_prime =False
            break
    
    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime")

check_prime(17)

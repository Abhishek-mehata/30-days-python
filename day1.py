# Day 1

# Problems
# Even or Odd
# Largest of 3 numbers

def even_or_odd():
    print("Even or Odd Module")
    num = int(input("Enter a number"))

    if num%2 == 0:
        print("It's an even number:")
    else:
        print("It is odd number")

even_or_odd()


def largest_among_three_numbers():
    print("Largest of 3 numbers module")
    num1 = int(input("Enter value for num1: "))
    num2 = int(input("Enter value for num2: "))
    num3 = int(input("Enter value for num3: "))
    
    greater = None
    if(num1>=num2 and num1>=num3):
        greater = num1
    elif num2>=num1 and num2>=num3:
        greater=num2
    elif num3>=num1 and num3>=num2:
        greater = num3
    elif num1==num2==num3:
        greater=num1
        print("All the entered numbers are equal")
    print("Greatest number is,", greater)


largest_among_three_numbers()


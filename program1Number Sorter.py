# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

print("Hello, kindly put your 4 numbers below for me to arrange it from highest to lowest.")

no1= float(input("Enter your first number: "))
no2= float(input("Enter your second number: "))
no3= float(input("Enter your third number: "))
no4= float(input("Enter your fourth number: "))

def high_to_low(num1, num2, num3, num4):
    if high == num1:
        if num2 > num3 and num3 > num4:
            print(f"Thank you! Your result is as follows: {num1}, {num2}, {num3}, and {num4}.")
        elif num2 < num3 and num3 > num4:
            print(f"Thank you! Your result is as follows: {num1}, {num3}, {num2}, and {num4}.")
        elif num2 < num3 and num3 < num4:
            print(f"Thank you! Your result is as follows: {num1}, {num3}, {num4}, and {num2}.")
        else:
            print(f"Thank you! Your result is as follows: {num1}, {num4}, {num2}, and {num3}.")
            return high

high = high_to_low(num1 = no1, num2 = no2, num3 = no3, num4 = no4)
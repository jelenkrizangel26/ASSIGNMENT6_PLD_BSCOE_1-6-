# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

# Steps
# 1. Introduce your program

from random import randrange
pg_name = "☆☆ Krizzy's Addition Quiz ☆☆"
print(" ╔══════════ஜ۩۞۩ஜ══════════╗")
print(pg_name)
print(" ╚══════════ஜ۩۞۩ஜ══════════╝")
print("\nGood day, welcome to my addition quiz. Try now to test your math skills!")

# 2. Ask the name
player = input("\nKindly put your name here: ")

print(f"Hello {player}, hope you're ready for this exciting quiz!")
print("Now, let's start the quiz!")

bestScore = 10
pScore = 0

quantity = 1
while quantity <= 10:
    rand1 = randrange(0, 99)
    rand2 = randrange(0, 99)
    sum = rand1 + rand2
    print(f"\n ☆☆ Question No. {quantity}☆☆ ")
    print(f"{str(rand1)} + {str(rand2)}")
    ans = int(input("Your answer: "))



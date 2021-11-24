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
print("\nGood day, welcome to my addition quiz. Try now, to test your math skills!")

# 2. Ask the name
player = input("\nKindly put your name here: ")

print(f"Hello {player}, hope you're ready for this exciting quiz!")
print("Now, let's start the quiz!")

bestScore = 0
pScore = 0


while bestScore <= 9:
    bestScore += 1
    rand1 = randrange(0, 99)
    rand2 = randrange(0, 99)
    sum = rand1 + rand2
    print(f"\n☆☆ Question No. {bestScore}☆☆ ")
    print(f"{str(rand1)} + {str(rand2)}")
    ans = int(input("Your answer: "))
    if int(ans) == sum:
        pScore += 1
        print("Excellent! Your answer is correct!（*^_^*)")
    else:
        print(f"Your answer is incorrect! The answer is {sum}, (×_×)")
        bestScore += 0
print(f"\nYou got {pScore} out of {bestScore} questions correct")
if pScore == 10:
    print(f"\nCongratulations {player}! You are already expert in adding numbers! ┍ლ(╹◡╹ლ)")
elif pScore >= 6 and pScore <=9:
    print(f"\nYou've done a great job {player}! Practice more and come back to perfect this quiz! (^_^)")
else:
    if pScore <= 5:
        print(f"\nSadly you failed the quiz {player} へ（>_<へ), I think you need to focus on adding numbers!")
        print("Better luck next time （*^_^*)")


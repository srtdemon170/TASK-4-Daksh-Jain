# ------------------------------------------
# Project 4: General Knowledge Quiz
# Author: Daksh Jain
# ------------------------------------------

print("=" * 50)
print("         GENERAL KNOWLEDGE QUIZ")
print("=" * 50)

score = 0

# Question 1
answer = input("\n1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
answer = input("\n2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Question 3
answer = input("\n3. Which is the largest ocean on Earth? ").strip().lower()

if answer == "pacific ocean" or answer == "pacific":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Pacific Ocean.")

print("\n" + "=" * 50)
print(f"Your Final Score: {score}/3")
print("=" * 50)

if score == 3:
    print("Outstanding! Perfect Score!")
elif score == 2:
    print("Great Job!")
elif score == 1:
    print("Good Try! Keep Learning.")
else:
    print("Better Luck Next Time!")
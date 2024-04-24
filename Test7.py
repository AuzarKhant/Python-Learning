answer = 2
guess = int(input("Enter your guess within 1 to 10 : "))
if guess > answer:
    print("Wrong! Try Lower")
elif guess < answer:
    print("Wrong! Try Higher")
elif guess == answer:
    print("Correct!!")
else:
    print("Invalid guess, Please try again!")

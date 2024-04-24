import random
coin_result = random.randint(1,2)

choice = int(input("Enter your choice! (1 for head/2 for tail) : "))

if choice == 1 and coin_result == 1:
    print("It's Head! You win!")
elif choice == 1 and coin_result ==2:
    print("It's Tail! You lose!")
elif choice == 2 and coin_result == 2:
    print("It's Tail! You win!")
elif choice == 2 and coin_result == 1:
    print("It's Head! You Lose!")
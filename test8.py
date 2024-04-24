answer = input("""
   Enter the weather
 (Rainy, sunny, windy)
""")
if answer == "rainy":
    print("It's raining, Please take an Umbrella!")
elif answer == "sunny":
    print("It's raining, Please stay hydrated!")
elif answer == "windy":
    print("It's windy, Please drive carefully!")
else:
    print("weather not invalid, Please choose rainy, sunny or windy!")
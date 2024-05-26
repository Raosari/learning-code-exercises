import random


num_to_Guess = random.randint(1, 10)




while True:
    try:
        user_guess = int(input("Guess a number  "))
        if not 0 < user_guess < 11:
            print("I said between 1 and 10")

        elif user_guess != num_to_Guess:
            print("That's not my number...Try again")

        else:
            print(f'Well done, the number what i was thinking is {num_to_Guess}')
            break

    except ValueError:
        print("Introduce numbers")
        continue

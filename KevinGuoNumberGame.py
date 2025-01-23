import random
import time

def guess_number_game():
    print("Welcome to Kevin Guo's Game!!!")
    print("You can choose difficulty: \n1. Easy Mode (1-50, 10Attempts)\n2. Median Mode (1-100, 8Attempts)\n3. Kevin's Mode (1-200, 6Attempts)")
    
    while True:
        difficulty = input("Please select your difficulty (1/2/3): ")
        if difficulty in ['1', '2', '3']:
            break
        print("please choose your level 1, 2, or 3")

    if difficulty == '1':
        max_number = 50
        max_attempts = 10
    elif difficulty == '2':
        max_number = 100
        max_attempts = 8
    else:
        max_number = 200
        max_attempts = 6

    number_to_guess = random.randint(1, max_number)
    attempts = 0
    start_time = time.time()

    print(f"\n I've got a number from 1 to {max_number}，You have {max_attempts} attempts。")
    
    while attempts < max_attempts:
        attempts += 1
        user_guess = input(f" {attempts} Attempts，please type in your guess number: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please type in a valid integer")
            continue

        if user_guess < number_to_guess:
            print("Man, that is too low！")
        elif user_guess > number_to_guess:
            print("Oh, that might be too high！")
        else:
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)
            print(f"\nCongrats! You got it, number is {number_to_guess}.")
            print(f"You've attempted {attempts} times, with {time_taken} seconds.")
            print(f" Your score: {1000 // (attempts * max(1, time_taken // 5))}")
            break

        if attempts == max_attempts - 2:
            print("Reminder: this is an even number!" if number_to_guess % 2 == 0 else "Reminder: this is an odd number!")

    else:
        print(f"\n Well what a pity, you've used all {max_attempts} attempts. The correct number is {number_to_guess}.")

    print("Game Over, see you later.")

if __name__ == "__main__":
    guess_number_game()

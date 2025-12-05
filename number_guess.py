import random

print("🎯 Welcome to the Number Guessing Game!")

# Generate random number between 1 and 20
secret_number = random.randint(1, 20)

attempts = 0
guess = None

while guess != secret_number:
    try:
        guess = int(input("👉 Guess a number between 1 and 20: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too Low! Try again.\n")
        elif guess > secret_number:
            print("📈 Too High! Try again.\n")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"🔥 You guessed it in {attempts} attempts!")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

print("\nThanks for playing 😊")


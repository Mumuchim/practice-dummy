secret = 9
guess_count = 3
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    if guess == secret:
        print("You win!")
        break

else:
    print("Sorry, you lose.")

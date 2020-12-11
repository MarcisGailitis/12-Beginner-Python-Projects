import random


def guess_computer(minint, maxint, random_number):
    count = int()
    guess = int()

    while random_number != guess:
        guess = random.randint(minint, maxint)
        count += 1

        if guess < random_number:
            print(f'Guess nr {count}: AI guessed {guess}, too low')
            minint = guess

        elif guess > random_number:
            print(f'Guess nr {count}: AI guessed {guess}, too high')
            maxint = guess

    else:
        print(f'Guess nr {count}: AI guessed {guess}, Success!')


if __name__ == "__main__":
    minint = 1
    maxint = 100
    secret_number = int(input(f'Enter a number b/w {minint} and {maxint}: '))
    guess_computer(minint, maxint, secret_number)

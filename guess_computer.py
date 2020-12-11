import random


def guess_computer(minint, maxint):
    count = int()
    guess = int()
    random_number = random.randint(minint, maxint)

    print(f'Guess the nr b/w {minint} and {maxint}')
    while guess != random_number:
        guess = int(input('Guess a number: '))
        count += 1
        if guess > random_number:
            print(f'Guess nr {count}: Your guess is too high')
        elif guess < random_number:
            print(f'Guess nr {count}: Your guess is too small')
        elif guess == random_number:
            print(f'Guess nr {count}: Success')


if __name__ == "__main__":
    minint = 1
    maxint = 100
    guess_computer(minint, maxint)

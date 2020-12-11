guess_word = True
guess_letter = True

while guess_word:

    counter = 0
    word_out = []
    guessed_letters = set()
    word = input('Enter the word for hangman game: ')
    letter_list = set(word)

    print(f'\nGuess the following word: {"* " * len(word)}')

    while guess_letter:

        print(
            f'You have used following letters: {", ".join(guessed_letters)}')
        counter += 1
        input_letter = input(
            f'\nTry Nr {counter}. Enter a letter or quit to exit: ')

        if input_letter == 'quit':
            break

        if input_letter in guessed_letters:
            print('You already guessed that letter')
        else:
            guessed_letters.add(input_letter)

        for letter in word:
            if letter in guessed_letters:
                word_out.append(letter)
            else:
                word_out.append('*')

        print(f'Guess the following word: {" ".join(word_out)}')

        if letter_list == set(word_out):
            print('Success!')
            guess_letter = False

        word_out.clear()

    cont = input('Another (y/n)?: ')
    if cont in ('n', 'no'):
        guess_word = False

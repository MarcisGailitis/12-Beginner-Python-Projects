guess_word = True
guess_letter = True

while guess_word:
    word = input('Enter the word')
    print(word)

    word_out = []
    guessed_letters = set()

    letter_list = set(word)
    print("".join(letter_list))

    while guess_letter:
        print(
            f'You have guessed following letters: {"".join(guessed_letters)}')
        input_letter = input('enter letter: ')
        if input_letter in guessed_letters:
            print('You already guessed that letter')
        else:
            guessed_letters.add(input_letter)

        for letter in word:
            if letter in guessed_letters:
                word_out.append(letter)
            else:
                word_out.append('*')

        print("".join(word_out))

        if letter_list == set(word_out):
            print('Success!')
            guess_letter = False

        word_out = []

    cont = input('another?')
    if cont in ('n', 'no'):
        guess_word = False

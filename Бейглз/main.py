import random

NUM_DIGITS = 3 # (!) Попробуйте задать эту константу равной 1 или 10
MAX_GUESSES = 3 # (!) Попробуйте задать эту константу равной 1 или 100

def main():
    print('''Рогалики, дедуктивно-логическая игра.
Автор: Эл Свейгарт al@inventwithpython.com

Я придумал {}-значное число без повторяющихся цифр.
Попробуйте угадать, что это за число. Вот несколько подсказок:
Когда я говорю:    Это означает:
Pico -              одна цифра правильная, но в неправильном положении.
Fermi -             одна цифра правильная и находится в правильном положении.
Bagels -            ни одна цифра не верна.

Например, если секретное число было 248, а ваше предположение - 843, то
подсказками могут быть Ферми-Пико."'.format(NUM_DIGITS))''')
    while True: # Основной цикл игры
        # Переменная, в которой хранится секретное число которое должен угадать игрок
        secretNum = getSecretNum()
        print("Я придумал число.")
        print("Вы можете попробовать угадать это {} - значное число.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Продолжаем итерации до получения правильной догадки:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Правильно, выходим из цикла.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        # Спрашиваем игрока, хочет ли он сыграть еще раз.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')


def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789')  # Создает список цифр от 0 до 9.
    random.shuffle(numbers)  # Перетасовываем их случайным образом.

    # Берем первые NUM_DIGITS цифр списка для нашего секретного числа:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        return secretNum


def getClues(guess, secretNum):
    """Возвращает строку с подсказками pico, fermi и bagels
    для полученной на входе пары из догадки и секретного числа."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на правильном месте.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Правильная цифра на неправильном месте.
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'  # Правильных цифр нет вообще.
    else:
        # Сортируем подсказки в алфавитном порядке, чтобы их исходный
        # порядок ничего не выдавал.
        clues.sort()
        # Склеиваем список подсказок в одно строковое значение.
        return ' '.join(clues)

# Если программа не импортируется, а запускается, производим запуск:

if __name__ == '__main__':
    main()
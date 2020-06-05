import os
import random

BASEPATH = os.path.dirname(__file__)


def init():
    print("Init Hangman Game")
    print("You have 5 chances of error to guess the name of the Anime")
    chances = 5
    sorting_word = get_word()
    hits_list = ["_" for letter in sorting_word]
    print(sorting_word)
    print("The Anime have {} words".format(len(sorting_word)))
    print(' '.join(hits_list))

    while True:
        letter = input("What letter ? ").strip()
        position = sorting_word.find(letter)

        if position < 0:
            print('Letter not found !!')
            chances -= 1
            print('You have {} chances !!'.format(chances))
        else:
            print("letter found !!")
            index_letter = 0
            for letters in sorting_word:
                if letter.upper() == letters.upper():
                    hits_list[index_letter] = letter
                index_letter += 1
            print(' '.join(hits_list))

        if chances == 0:
            print("You use all chances !! Game Over !!")
            print("The Anime is {}".format(sorting_word))
            break

        if "_" not in hits_list:
            print("You got the word right !! Game win !!")
            break
    print("Final Game !!")


def get_word():
    file = open(BASEPATH + '/words.dat', 'r')
    words = file.readlines()
    file.close()
    random_word = random.randrange(0, len(words))
    return words[random_word].strip()


if __name__ == "__main__":
    init()

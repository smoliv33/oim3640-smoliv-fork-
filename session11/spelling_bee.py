# https://www.nytimes.com/puzzles/spelling-bee

from word_sol import uses_only


def spell_bee(required, available):
    f = open('data/words.txt')
    for line in f:
        word = line.strip()
        # if the word has 4 or more letters and contains the center/required letter and uses only the available letters
        if len(word) >= 4 and required in word and uses_only(word, available):
            print(word)


def main():
    centered_letter = "e"
    available_letters = "otblci"
    spell_bee(required=centered_letter, available=available_letters + centered_letter)


if __name__ == "__main__":
    main()

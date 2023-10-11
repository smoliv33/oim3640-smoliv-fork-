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
    required_letter = ""
    available_letters = ""
    spell_bee(required=required_letter, available=available_letters)


if __name__ == "__main__":
    main()

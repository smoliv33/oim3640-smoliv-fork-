def histogram(s):
    """return a dict, key is letter, value is frequency"""
    d = {}
    for letter in s:
        # if letter not in d:
        #     d[letter] = 1
        # else:
        #     d[letter] += 1
        print(f'Now checking {letter}')
        print(f'Current count: {d.get(letter, 0)}')
        d[letter] = d.get(letter, 0) + 1
        print(d)
        print()
    return d


print(histogram('larrrrrrrry')) 
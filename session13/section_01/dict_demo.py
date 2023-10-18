def count(s):
    d = {}
    for c in s:
        # if c not in d:
        #     d[c] = 1
        # else:
        #     d[c] += 1
        print(f'Now checking {c}. ')
        print(f'frequency for {c} is {d.get(c, 0)}')
        d[c] = d.get(c, 0) + 1
        print('after adding frequency', d)
    return d


print(count('fede'))
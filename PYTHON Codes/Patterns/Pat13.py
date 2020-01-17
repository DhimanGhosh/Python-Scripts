'''
5 4 3 2 1
  4 3 2 1
    3 2 1
      2 1
        1
'''

s = 0
for i in range(1, 6)[::-1]:
    print(' '*s, end='')
    for j in range(1, i+1)[::-1]:
        print('{}'.format(j), end=' ')
    s += 2
    print()
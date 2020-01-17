'''
        1
      3 2 1
    5 4 3 2 1
  7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
'''

freq = 1
for i in range(0, 5)[::-1]:
    print(' '*i*2, end='')
    for j in range(1, freq+1)[::-1]:
        print(j, end=' ')
    freq += 2
    print()
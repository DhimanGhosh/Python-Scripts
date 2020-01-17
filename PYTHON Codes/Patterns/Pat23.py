'''
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
'''

freq = 1
for i in range(0, 5)[::-1]:
    print(' '*i*2, end='')
    for j in range(1, freq+1):
        print(j, end=' ')
    freq += 2
    print()
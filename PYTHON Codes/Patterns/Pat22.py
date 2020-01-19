'''
        1
      3 3 3
    5 5 5 5 5
  7 7 7 7 7 7 7
9 9 9 9 9 9 9 9 9
'''

val = freq = 1
for i in range(0, 5)[::-1]:
    print(' '*i*2, end='')
    for j in range(freq):
        print(val, end=' ')
    val += 2
    freq += 2
    print()
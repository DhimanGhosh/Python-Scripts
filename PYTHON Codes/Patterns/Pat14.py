'''
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
'''

val = 1
for i in range(0, 5)[::-1]:
    print(' '*i*2, end='')
    for j in range(1, val+1):
        print(val, end=' ')
    val += 1
    print()
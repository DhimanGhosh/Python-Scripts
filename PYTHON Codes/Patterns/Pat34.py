'''
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
'''

val = 1
for i in range(0, 5)[::-1]:
    print(' '*i, end='')
    for j in range(i, 5):
        print(val, end=' ')
    val += 1
    print()

val -=2
s = i+1
for i in range(1, 5)[::-1]:
    print(' '*s, end='')
    for j in range(i):
        print(val, end=' ')
    val -= 1
    s += 1
    print()
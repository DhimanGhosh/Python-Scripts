'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''

val = 1
for i in range(0, 5)[::-1]:
    print(' '*i, end='')
    for j in range(1, val+1):
        print(j, end=' ')
    val += 1
    print()
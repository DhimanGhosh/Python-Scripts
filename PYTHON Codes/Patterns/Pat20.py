'''
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
'''

s = 0
for i in range(1, 6)[::-1]:
    print(' '*s, end='')
    for j in range(1, i+1):
        print(j, end=' ')
    s += 1
    print()
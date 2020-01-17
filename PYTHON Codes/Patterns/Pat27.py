'''
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1
'''

s = 0
for i in range(1, 6)[::-1]:
    print(' '*s*2, end='')
    
    for j in range(i):
        print(i, end=' ')
    
    for j in range(i-1):
        print(i, end=' ')
    
    s += 1
    print()
'''
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
'''

s = 0
for i in range(1, 6)[::-1]:
    print(' '*s*2, end='')
    
    for j in range(1, i+1):
        print(j, end=' ')
    
    for k in range(j+1, j+i):
        print(k, end=' ')
    
    s += 1
    print()
'''
9 9 9 9 9 9 9 9 9
  7 7 7 7 7 7 7
    5 5 5 5 5
      3 3 3
        1
    
'''

s = 0
for i in range(1, 6)[::-1]:
    print(' '*s*2, end='')
    
    for j in range(i):
        print(i*2-1, end=' ')
    
    for j in range(i-1):
        print(i*2-1, end=' ')
    
    s += 1
    print()
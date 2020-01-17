'''
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''

s = 4
for i in range(1, 6):
    print(' '*s*2, end='')

    for j in range(1, i+1):
        print(j, end=' ')
    
    for j in range(1, i)[::-1]:
        print(j, end=' ')
    
    s -= 1
    print()
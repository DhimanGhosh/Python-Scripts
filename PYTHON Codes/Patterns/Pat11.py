'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''

for i in range(1, 6)[::-1]:
    for j in range(i, 6)[::-1]:
        print(j, end=' ')
    print()
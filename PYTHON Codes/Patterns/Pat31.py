'''
3
2 3
1 2 3
0 1 2 3
1 2 3
2 3
3
'''

for i in range(0, 4)[::-1]:
    for j in range(i, 4):
        print(j, end=' ')
    print()

for i in range(1, 4):
    for j in range(i, 4):
        print(j, end=' ')
    print()
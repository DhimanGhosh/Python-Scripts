'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

for i in range(1, 6)[::-1]:
    for j in range(i):
        print(i, end=' ')
    print()
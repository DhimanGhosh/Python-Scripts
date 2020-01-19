'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''

val = 1
for i in range(1, 6)[::-1]:
    for j in range(i):
        print(val, end=' ')
    val += 1
    print()
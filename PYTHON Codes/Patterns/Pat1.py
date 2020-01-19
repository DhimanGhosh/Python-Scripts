'''
1
2 3
4 5 6
7 8 9 10
'''

val = 1
for i in range(1, 6):
    for j in range(i):
        print(val, end=' ')
        val += 1
    print()
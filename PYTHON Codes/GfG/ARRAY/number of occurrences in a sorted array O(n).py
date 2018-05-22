'''
Count number of occurrences (or frequency) in a sorted array

Input: arr[] = {1, 1, 2, 2, 2, 2, 3}   x = 2
Output: 4 // x (or 2) occurs 4 times in arr[]

Input: arr[] = {1, 1, 2, 2, 2, 2, 3}   x = 3
Output: 1 

Input: arr[] = {1, 1, 2, 2, 2, 2, 3}   x = 1
Output: 2 

Input: arr[] = {1, 1, 2, 2, 2, 2, 3}   x = 4
Output: -1 // 4 doesn't occur in arr[] 
'''

def index(a, x, i, n):
    if i == n-1 and a[i] != x:
        return -1
    elif a[i] != x:
        return index(a, x, i+1, n)
    else:
        return i

def count(a, x, n):
    f = index(a, x, 0, n)
    if f==-1:
        return f
    a.reverse()
    l = index(a, x, 0, n)
    return n-l - f

def run():
    arr = [1, 1, 2, 2, 2, 2, 3]
    x = 4
    print('Array:\t\t' + str(arr) + '\nx:\t\t' + str(x) + '\nOccurrence:\t', end='')
    c = count(arr, x, len(arr))
    print(c) if c!=-1 else print('Num Not Found!')

if __name__ == '__main__':
    run()

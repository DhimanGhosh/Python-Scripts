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

def first(a, x, l, h, n):
    if l<=h:
        mid = (l + h)//2
        if (mid == 0 or x > a[mid-1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return first(a, x, mid+1, h, n)
        else:
            return first(a, x, l, mid-1, n)
    return -1

def last(a, x, l, h, n):
    if l<=h:
        mid = (l + h)//2
        if (mid == n-1 or x < a[mid+1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return last(a, x, l, mid-1)
        elif x < a[mid]:
            return last(a, x, mid+1, h)
    return -1

def count(a, x, n):
    f = first(a, x, 0, n-1, n)
    if f==-1:
        return f
    l = last(a, x, f, n-1, n)
    return l - f + 1

def run():
    arr = [1, 1, 2, 2, 2, 2, 3]
    x = 2
    print('Array:\t\t' + str(arr) + '\nx:\t\t' + str(x) + '\nOccurrence:\t', end='')
    print(count(arr, x, len(arr)))

if __name__ == '__main__':
    run()

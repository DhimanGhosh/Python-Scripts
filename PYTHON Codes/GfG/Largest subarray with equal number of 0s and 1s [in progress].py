'''
Largest subarray with equal number of 0s and 1s

Input: arr[] = {1, 0, 1, 1, 1, 0, 0}
Output: 1 to 6 (Starting and Ending indexes of output subarray)

Input: arr[] = {1, 1, 1, 1}
Output: No such subarray

Input: arr[] = {0, 0, 1, 1, 0}
Output: 0 to 3 Or 1 to 4
'''

from List import List

def chk_sum(arr, f, l):
    a1 = List(arr)
    zero_count = a1.count(0)
    one_count = a1.count(1)
    flag = False
    if zero_count == one_count:
        flag = True
    return [f, l, flag]

def largest_subarray(arr):
    if chk_sum(arr, 0, len(arr)-1)[2]:
        return [0, len(arr)-1]
    
    n = len(arr)
    for i in range(n-1, -1, -1):
        f = 0
        l = i
        while f<=l:
            cs = chk_sum(arr[f:l], f, l-1)
            if cs[2]:
                return cs[:-1]
            else:
                f+=1

    for i in range(n):
        f = i
        l = n
        while f<=l:
            cs = chk_sum(arr[f:l], f, l-1)
            if cs[2]:
                return cs[:-1]
            else:
                l-=1

    return -1
    
def run():
    arr = [1, 1, 1, 1]
    
    subs = largest_subarray(arr)
    if subs!=-1:
        print('{} to {}'.format(subs[0],subs[1]))
    else:
        print('No such subarray!')

if __name__ == '__main__':
    run()

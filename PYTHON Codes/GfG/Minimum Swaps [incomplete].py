'''
Input:  arr[] = {2, 1, 5, 6, 3}, k = 3
Output: 1

Explanation: 
To bring elements 2, 1, 3 together, swap 
element '5' with '3' such that final array
will be-
arr[] = {2, 1, 3, 6, 5}

Input:  arr[] = {2, 7, 9, 5, 8, 7, 4}, k = 5
Output: 2
'''

from List import List

def sort(a, k):
    al = List(a)
    c = 0
    if al.inside(k) == False:
        return -1
    else:
        for i in range(len(a)):
            pos = al.find_num_pos(k)
            for j in range(len(a)-i-1):
                if a[j]>k:
                    a[j],a[pos]=a[pos],a[j]
                    c += 1
    return c

def __chk_list(a, k):
    flag = False
    for i in range(len(a)):
        if a[i]<=k:
            flag = True
            break
    return flag

def swaps(a, k):
    al = List(a)
    if al.inside(k) == False:
        return -1
    else:
        pos = al.find_num_pos(k)
        c = 0
        for i in range(len(a)):
            if a[i]>k and __chk_list(a[i+1:], k):
                a[i], a[pos] = a[pos], a[i]
                pos = i
                c += 1
    return c
        

def run():
    arr = [2, 7, 9, 5, 8, 7, 4]
    k = 5
    s = sort(arr, k)
    if s!=-1:
        print(s)
    else:
        print(str(k)+': Not present in input list!')

if __name__ == '__main__':
    run()

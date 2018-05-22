'''
Question:
Find a sorted subsequence of size 3 in linear time

Description:
Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k in 0(n) time.
If there are multiple such triplets, then print any one of them.

Example:
Input:  arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30

Input:  arr[] = {1, 2, 3, 4}
Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4

Input:  arr[] = {4, 3, 2, 1}
Output: No such triplet
'''
def min_index(a, index):
    k, p = (a[index], index)
    for i in range(index, len(a)):
        if a[i]<k:
            k = a[i]
            p = i
    return [k, p]

def max_index(a, index):
    k, p = (a[index], index)
    for i in range(index, len(a)):
        if a[i]>k:
            k = a[i]
            p = i
    return [k, p]

def subsequence(a):
    i = min_index(a, 0)
    j = max_index(a, i[1])
    k = max_index(a, j[1])

    if i[1] < j[1] < k[1]:
        return [i[0], j[0], k[0]]
    else:
        return None

def run():
    arr = [12, 11, 10, 5, 6, 2, 30]
    print(arr)
    subs = subsequence(arr)
    if subs != None:
        print(subs)
    else:
        print('No such triplet')

if __name__ == '__main__':
    run()

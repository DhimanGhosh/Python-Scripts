'''
Alternative Sorting

Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
Output : 7 1 6 2 5 3 4

Input : arr[] = {1, 6, 9, 4, 3, 7, 8, 2}
Output : 9 1 8 2 7 3 6 4
'''

def alt_sort(a):
    a.sort()
    arr = a
    a.reverse()
    rev = a

    l_arr = len(arr)
    l_rev = len(rev)

    l = (l_arr<l_rev)?l_arr:l_rev
    

def run():
    arr = [7, 1, 2, 3, 4, 5, 6]
    print(arr)
    print(alt_sort(arr))

if __name__ == '__main__':
    run()

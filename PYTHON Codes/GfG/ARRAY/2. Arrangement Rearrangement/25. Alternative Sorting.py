'''
Alternative Sorting

Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
Output : 7 1 6 2 5 3 4

Input : arr[] = {1, 6, 9, 4, 3, 7, 8, 2}
Output : 9 1 8 2 7 3 6 4
'''

'''def alt_sort_lambda(a):
    a.sort()
    a.reverse()
    return [v for i,v in enumerate(a) if i%2==0] + [v for i,v in enumerate(a, start=len(a)-1) if i%2==0]
'''
def alt_sort(a):
    a.sort()
    a.reverse()

    p = 0
    arr = [0]*len(a)
    for i in range(len(a)):
        if i%2 == 0 and arr[i]==0:
            arr[i] = a[p]
            p+=1

    for i in range(len(a)-1, 0, -1):
        if arr[i]==0:
            arr[i] = a[p]
            p+=1
    
    return arr

def run():
    arr = [0, 1, 2, 0, -1, 5, 6, 0]
    print(arr)
    print(alt_sort(arr))
    #print(alt_sort_lambda(arr))

if __name__ == '__main__':
    run()

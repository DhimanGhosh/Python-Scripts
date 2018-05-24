'''
Given an array A[] having distinct elements,
the task is to find the next greater element for each element of the array in order of their appearance in the array.
If no such element exists, output -1.

Example:
Input
1 3 2 4 

Output
3 4 4 -1

Explanation
In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist hence -1.
'''

def next_grt(a):
    a1 = []
    for i in range(len(a)-1):
        flag = False
        for j in range(i+1, len(a)):
            if a[j] > a[i]:
                flag = True
                break
        if flag:
            a1.append(a[j])
        else:
            a1.append(-1)
    a1.append(-1)
    return a1

def run():
    arr = [11, 13, 3, 21]
    print(arr)
    print(next_grt(arr))

if __name__ == '__main__':
    run()

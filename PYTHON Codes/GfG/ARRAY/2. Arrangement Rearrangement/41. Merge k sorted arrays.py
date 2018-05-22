'''
Q. Merge k sorted arrays

Description:
Given k sorted arrays of size n each, merge them and print the sorted output.


Example:

Input:
k = 3, n =  4
arr[][] = { {1, 3, 5, 7},
            {2, 4, 6, 8},
            {0, 9, 10, 11}} ;

Output: 0 1 2 3 4 5 6 7 8 9 10 11 
'''
def form_matrix_from_array(a, n, k):
    arr = []
    for i in range(k):
        temp = []
        for j in range(n):
            temp.append(a[j+n*i])
        arr.append(temp)
    return arr

def print_array(a):
    for n in a:
        print(n,end=' ')
    print()

def print_matrix(a, n, k):
    for i in range(k):
        print_array(a[i])

def merge(a, k):
    arr = []
    for i in range(k):
        arr.extend(a[i])
    arr.sort()
    return arr

def run():
    arr = [[1, 3, 5, 7],
           [2, 4, 6, 8],
           [0, 9, 10, 11]]
    k = len(arr)
    n = 4
    output = merge(arr, k)

    print("\nOriginal Matrix is:")
    print_matrix(arr, n, k)
 
    print("\nMerged Array is:")
    print_array(output)

    matrix = form_matrix_from_array(output, n, k)
    print("\nSorted Matrix is:")
    print_matrix(matrix, n, k)

if __name__ == '__main__':
    run()

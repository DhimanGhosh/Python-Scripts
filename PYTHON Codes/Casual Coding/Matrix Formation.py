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
        print(n,end='\t')

def print_matrix(a, n, k):
    for i in range(k):
        print_array(a[i])
        print()
        print()

def run():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    n = 4
    k = 3
    arr = form_matrix_from_array(a, n, k)
    print_matrix(arr, n, k)

if __name__ == '__main__':
    run()

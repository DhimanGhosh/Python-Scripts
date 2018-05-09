'''
Even positioned are greater than Odd

Input : A[] = {1, 2, 2, 1}
Output : 1 2 1 2

Input : A[] = {1, 3, 2}
Output : 1 3 2

Input : A[] = {1, 3, 2, 2, 5}
Output : 1 5 2 3 2
'''

def find_num_pos(n, a, eo='e'):
    for i in range(len(a)):
        if eo == 'e':
            if a[i] <= n:
                return i
        elif eo == 'o':
            if a[i] >= n:
                return i

def rearrange(arr):
    for i in range(len(arr), 2):
        if i%2 == 0:
            pos = find_num_pos(a[i], arr[i:]) + i
            if arr[pos] >= arr[i]:
                arr[i], arr[pos] = arr[pos], arr[i]
        else:
            pos = find_num_pos(a[i], arr[i:], 'o') + i
            if arr[pos] <= arr[i]:
                arr[i], arr[pos] = arr[pos], arr[i]

def run():
    arr = [1, 3, 2, 2, 5]
    print(arr)
    rearrange(arr)
    print(arr)

if __name__ == '__main__':
    run()

'''
Even numbers at even index and odd numbers at odd index

Input : arr[] = {10, 9, 7, 18, 13, 19, 4, 20, 21, 14}
Output : 10 9 18 7 20 19 4 13 14 21

Input : arr[] = {3, 6, 12, 1, 5, 8}
Output : 6 3 12 1 8 5
'''

def find_num_pos(a, eo='e'):
    for i in range(len(a)):
        if eo == 'e':
            if a[i]%2 == 0:
                return i
        elif eo == 'o':
            if a[i]%2 != 0:
                return i

def rearrange(arr):
    for i in range(len(arr)-1):
        if i%2 == 0 and arr[i]%2 != 0:
            pos = find_num_pos(arr[i:]) + i
            arr[i], arr[pos] = arr[pos], arr[i]
        elif i%2 != 0 and arr[i]%2 == 0:
            pos = find_num_pos(arr[i:], 'o') + i
            arr[i], arr[pos] = arr[pos], arr[i]

def run():
    arr = [3, 6, 12, 1, 5, 8]
    print(arr)
    rearrange(arr)
    print(arr)

if __name__ == '__main__':
    run()

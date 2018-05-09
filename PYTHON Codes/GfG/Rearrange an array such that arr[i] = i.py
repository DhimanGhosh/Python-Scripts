def find_num_pos(a, n):
    for i in range(len(a)):
        if a[i] == n:
            return i

def rearrange(arr):
    for i in range(len(arr)):
        if i in arr:
            pos = find_num_pos(arr, i)
            arr[pos], arr[i] = arr[i], arr[pos]

def run():
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    print(arr)
    rearrange(arr)
    print(arr)

if __name__ == '__main__':
    run()

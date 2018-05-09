def segregate(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            arr[i], arr[k] = arr[k], arr[i]
            k+=1
    return arr

def run():
    arr = [7, 10, 2, 3, 6, 9, 4, 1]
    print(arr)
    print(segregate(arr))

if __name__ == '__main__':
    run()

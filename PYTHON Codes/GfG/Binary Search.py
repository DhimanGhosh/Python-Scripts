def bin_srch(arr, num, low, high):
    if low<=high:
        mid = int((low + high)/2)

        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            return bin_srch(arr, num, low, mid-1)
        else:
            return bin_srch(arr, num, mid+1, high)
    return None

def run():
    a = [3, 7, 1 ,9, 2]
    print('Original: '+str(a))
    a.sort()
    print('Sorted: '+str(a))
    num = input('Num: ')
    srch = bin_srch(a, int(num), 0, len(a)-1)
    if srch!=None:
        print('Found!')
    else:
        print('Not Found!')

if __name__ == '__main__':
    run()

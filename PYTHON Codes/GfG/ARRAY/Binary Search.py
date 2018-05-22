def bin_srch(arr, num, low, high):
    if low<=high:
        mid = int((low + high)/2)
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            return bin_srch(arr, num, low, mid-1)
        return bin_srch(arr, num, mid+1, high)
    return -1

def run():
    a = [3, 7, 1 ,9, 2, 9]
    print('Original: '+str(a))
    a.sort()
    print('Sorted: '+str(a))
    num = int(input('Num: '))
    flag = False
    if num >= a[0] or num <= a[-1]:
        srch = bin_srch(a, int(num), 0, len(a)-1)
        if srch!=-1:
            flag = True
    if flag:
        print('Found at index: {}'.format(srch))
    else:
        print('Not Found!')

if __name__ == '__main__':
    run()

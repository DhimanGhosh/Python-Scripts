def get_closest(v1, v2, num):
    if (num - v1) > (v2 - num):
        return v2
    elif (num - v1) < (v2 - num):
        return v1
    elif (num - v1) == (v2 - num):
        choice = input('Ceil / Floor (c/f): ('+str(v2)+'/'+str(v1)+')? ')
        if choice=='f':
            return v1
        elif choice=='c':
            return v2
        else:
            print('Wrong Choice!')
            print('Returning Floor Value: '+str(v1))

def find_closest(arr, num):
    if num >= arr[-1]:
        return arr[-1]
    elif num<=arr[0]:
        return arr[0]
    else:
        low = 0
        high = len(arr)
        mid = 0
        while low <= high:
            mid = int((low + high)/2)
            if arr[mid] == num:
                return arr[mid]
            elif num < arr[mid]:
                if mid > 0 and num > arr[mid - 1]:
                    return get_closest(arr[mid - 1], arr[mid], num)
                high = mid
            else:
                if mid < len(arr) - 1 and num < arr[mid + 1]:
                    return get_closest(arr[mid], arr[mid + 1], num)
                low = mid + 1
        return arr[mid]

def run():
    arr = [1, 4, 6, 9]
    print(arr)
    num = input('Value: ')
    closest = find_closest(arr, int(num))
    if closest != None:
        print(closest)

if __name__ == '__main__':
    run()

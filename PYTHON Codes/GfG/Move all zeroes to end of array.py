'''
Move all zeroes to end of array

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6}
Output : 1 2 3 6 0 0 0

Input: arr[] = {0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9}
Output: 1 9 8 4 2 7 6 9 0 0 0 0 0
'''

def rearrange(a):
    last_pos = -1
    i = 0
    while i <= len(a):
        if i-len(a)==last_pos:
            break
        elif a[i] == 0:
            a = a[:i] + a[i+1:] + [0]
            last_pos -= 1
        else:
            i+=1
    return a

def run():
    arr = [1, 2, 0, 0, 0, 3, 6]
    print(arr)
    print(rearrange1(arr))

if __name__ == '__main__':
    run()


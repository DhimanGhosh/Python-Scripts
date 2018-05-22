'''
Move all zeroes to end of array

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6}
Output : 1 2 3 6 0 0 0

Input: arr[] = {0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9}
Output: 1 9 8 4 2 7 6 9 0 0 0 0 0
'''

def rearrange(a):
    return [z for z in a if z!=0] + [z for z in a if z==0]

def run():
    arr = [1, 2, 0, 0, 0, 3, 6]
    print(arr)
    print(rearrange(arr))

if __name__ == '__main__':
    run()


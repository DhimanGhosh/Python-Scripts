'''
Replace every array element by multiplication of previous and next

Example:
Input: arr[] = {2, 3, 4, 5, 6}
Output: arr[] = {6, 8, 15, 24, 30}

// We get the above output using following
// arr[] = {2*3, 2*4, 3*5, 4*6, 5*6}
'''

def replace(a):
    if len(a)==1:
        return a
    elif len(a)==2:
        return [a[0]*a[1]]*2
    else:
        prev = a[0]
        a[0] = prev*a[1]
        for i in range(1,len(a)-1):
            curr = a[i]
            a[i] = prev*a[i+1]
            prev = curr
        a[-1] = prev*a[-1]
        return a

def run():
    arr = [2, 3, 4, 5, 6]
    print(arr)
    print(replace(arr))

if __name__ == '__main__':
    run()

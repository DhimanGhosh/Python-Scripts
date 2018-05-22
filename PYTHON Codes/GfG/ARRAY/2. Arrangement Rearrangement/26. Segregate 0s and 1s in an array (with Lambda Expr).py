'''
Segregate 0s and 1s in an array

Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
'''

def segr(a):
    return [n for n in a if n==0] + [n for n in a if n==1]

def run():
    arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    print(arr)
    print(segr(arr))

if __name__ == '__main__':
    run()

def rotate(arr, r):
    return str(arr[r:]+arr[:r])+': Rotation Value = '+str(r)

def run():
    arr = list(input('Any Integer Number: '))
    arr = [int(n) for n in arr]
    print(arr)
    r = int(input('Rotation Value: ')) % len(arr)
    print(rotate(arr, r))

if __name__ == '__main__':
    run()






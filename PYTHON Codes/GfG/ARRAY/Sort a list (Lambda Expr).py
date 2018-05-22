def sort(a):
    h = lambda x:x[0]
    a.sort(key=h)
    return a

def run():
    arr = [(6, 8), (0, -2), (-8, 4), (-5, 0)]
    print(sort(arr))

if __name__ == '__main__':
    run()

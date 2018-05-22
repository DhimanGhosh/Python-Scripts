def rearrange(a):
    return [n for n in a if n<0] + [n for n in a if n==0] + [n for n in a if n>0]

def run():
    arr = [6, 8, 0, -2, -8, 4, -5, 0]
    print(arr)
    print(rearrange(arr))

if __name__ == '__main__':
    run()

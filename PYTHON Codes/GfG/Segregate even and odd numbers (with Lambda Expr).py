def segregate(arr):
    return [n for n in arr if n%2==0] + [n for n in arr if n%2!=0]

def run():
    arr = [7, 10, 2, 3, 6, 9, 4, 1]
    print(arr)
    print(segregate(arr))

if __name__ == '__main__':
    run()

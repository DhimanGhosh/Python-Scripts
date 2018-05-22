from time import gmtime, strftime, time

def randomize():
    current_mil_sec = int(round(time() * 1000))
    current_sec = int(strftime('%S', gmtime()))
    r = (current_sec % 100) * (current_mil_sec % 1000)
    return r

def rand_range(m, n):
    r = randomize()

    l = len(str(n))
    r = str(r)
    for i in range(len(r) - l):
        if int(r[i:(i+l)])>=m and int(r[i:(i+l)])<=n:
            return int(r[i:(i+l)])
    try:
        return rand_range(m, n)
    except:
        return n - (r//2)%10 + m
    return (m+n)//2

# Driver
def run():
    print(rand_range(0, 4))

if __name__ == '__main__':
    run()

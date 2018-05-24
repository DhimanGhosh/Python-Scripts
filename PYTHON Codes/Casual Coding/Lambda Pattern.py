def print_with_space(string):
    for c in string:
        print(c, end=' ')
    print()

def pattern_hour_glass(name):
    h = lambda x:x[:i]
    sp = 0
    for i in range(len(name), -1, -1):
        if i>0:
            print(' '*sp, end='')
            print_with_space(h(name))
            sp+=1
    sp-=2
    for i in range(len(name)+1):
        if i>1:
            print(' '*sp, end='')
            print_with_space(h(name))
            sp-=1

def run():
    height = 7
    item = '*'
    pattern = item * (height//2 + 1)
    pattern_hour_glass(pattern)

if __name__ == '__main__':
    run()

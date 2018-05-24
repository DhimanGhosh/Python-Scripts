def draw_A(h, item):
    s_sp = h - 1
    m_sp = 1
    print(' '*s_sp + item)
    s_sp -= 1
    for _ in range(h//2 - 1):
        print(' '*s_sp + item + ' '*m_sp, end=item)
        print()
        s_sp -= 1
        m_sp += 2
    print(' '*s_sp, end='')
    for _ in range(h//2 + 1):
        print(item + ' ', end='')
    print()
    s_sp -= 1
    m_sp += 2
    for _ in range(h//2):
        print(' '*s_sp + item + ' '*m_sp, end=item)
        print()
        s_sp -= 1
        m_sp += 2

def draw_B(h, item):
    m_sp = h - 2
    for _ in range(h//2): # TOP
        print(item + ' ', end='')
    print()
    for _ in range(h//2 - 1): # TOP_BAR
        print(item + ' '*m_sp + item)
    for _ in range(h//2): # MID
        print(item + ' ', end='')
    print()
    for _ in range(h//2 - 1): # BOTTOM_BAR
        print(item + ' '*m_sp + item)
    for _ in range(h//2): # BOTTOM
        print(item + ' ', end='')

def draw_C(h, item):
    print(' ', end='')
    for _ in range(h//2): # TOP
        print(' ' + item, end='')
    print()
    for _ in range(h - 1): # MID
        print(item)
    print(' ', end='')
    for _ in range(h//2): # BOTTOM
        print(' ' + item, end='')

def draw_D(h, item):
    m_sp = h - 2
    for _ in range(h//2): # TOP
        print(item + ' ', end='')
    print()
    for _ in range(h - 2): # BAR
        print(item + ' '*m_sp + item)
    for _ in range(h//2): # BOTTOM
        print(item + ' ', end='')

def draw_E(h, item):
    for _ in range(h//2 + 1): # TOP
        print(item + ' ', end='')
    print()
    for _ in range(h//2 - 1): # TOP_BAR
        print(item)
    for _ in range(h//2 + 1): # MID
        print(item + ' ', end='')
    print()
    for _ in range(h//2 - 1): # BOTTOM_BAR
        print(item)
    for _ in range(h//2 + 1): # BOTTOM
        print(item + ' ', end='')

def draw_X(h, item):
    s_sp = 0
    m_sp = h - 2

    for _ in range(h):
        print(' '*s_sp + item + ' '*m_sp, end=item)
        print()
        s_sp += 1
        m_sp -= 2
        if m_sp<1:
            print(' '*s_sp + item)
            break
    s_sp -= 1
    m_sp += 2
    for _ in range(h-1):
        print(' '*s_sp + item + ' '*m_sp, end=item)
        print()
        s_sp -= 1
        m_sp += 2
        if s_sp<0:
            break

def draw_Y(h, item):
    s_sp = 0
    m_sp = h - 2

    for _ in range(h):
        print(' '*s_sp + item + ' '*m_sp, end=item)
        print()
        s_sp += 1
        m_sp -= 2
        if m_sp<1:
            print(' '*s_sp + item)
            break
    for _ in range(h//2):
        print(' '*s_sp + item)

def draw_Z(h, item):
    s_sp = h - 2
    for _ in range(h//2 + 1):
        print(item + ' ', end='')
    print()
    for _ in range(h-2):
        print(' '*s_sp, end=item)
        print()
        s_sp -= 1
    
    for _ in range(h//2 + 1):
        print(item + ' ', end='')
    

def run():
    height = 9
    item = '*'
    draw_A(height, item)
    print('\n')
    draw_B(height, item)
    print('\n')
    draw_C(height, item)
    print('\n')
    draw_D(height, item)
    print('\n')
    draw_E(height, item)
    print('\n')
    draw_X(height, item)
    print('\n')
    draw_Y(height, item)
    print('\n')
    draw_Z(height, item)

if __name__ == '__main__':
    run()
    input('exit?')

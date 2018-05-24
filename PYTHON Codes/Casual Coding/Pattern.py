def draw_canvas(dim):
    for i in range(dim[0]):
        for j in range(dim[1]):
            print(canvas[i][j], end='')
        print()
    

def fill_canvas(item, dim):
    # Fill 'D'
    for i in range(6):
        canvas[i][i] = item
    k = i
    for i in range(5, 9):
        canvas[i][k] = item
        k-=1
    for i in range(10):
        canvas[i][0] = item

def draw(item, dimention):
    fill_canvas(item, dimention)
    draw_canvas(dimention)
   
def run(dimention):
    item = '*'
    draw(item, dimention)

if __name__ == '__main__':
    length = 45
    height = 9
    dimention = [length, height]
    canvas = [[' ' for _ in range(height)] for _ in range(length)]
    run(dimention)

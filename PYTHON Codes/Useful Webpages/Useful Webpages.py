urls = [line.rstrip('\n') for line in open('webpages.txt','r')]

def webpage(url):
    ur = url.split('//')[1]
    pg = ur.split('/')[0]
    if '.' in pg:
        res = pg.split('.')[1]
    else:
        res = pg
    res = res[0].upper() + res[1:]
    return res

def open_pages():
    os.system('TASKKILL /F /IM .exe')
    for u in urls:
        choice = input('Do you want to open '+webpage(u)+"(y/n): ")
        if choice=='y' or choice=='Y':
            webbrowser.open(u)

def run():
    open_pages()

if __name__ == '__main__':
    import webbrowser, os
    run()

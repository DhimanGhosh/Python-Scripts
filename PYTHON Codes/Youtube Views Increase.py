url = input('Enter YouTube URL: ')
refresh = input('Enter refresh rate(seconds): ')
views = input('Enter the number of views: ')

def OpenUrl():
    os.system('TASKKILL /F /IM .exe')
    webbrowser.open(url)
    print('Successfully Viewed!')
    time.sleep(int(refresh))

def run():
    for i in range(int(views)):
        OpenUrl()

if __name__ == '__main__':
    import webbrowser, time, os
    run()

from time import gmtime, strftime, time

def chk_palindrome(word):
    flag = True
    if word != word[::-1]:
        flag = False
    return flag

def longest_substring(word):
    if chk_palindrome(word):
        return word
    
    c = ''
    word_list = []
    for i in range(len(word)-1):
        c = word[i]
        for j in range(i+1,len(word)):
            if c == word[j] and chk_palindrome(word[i:j+1]):
                word_list.append(word[i:j+1])
    
    if len(word_list)>0:
        w1=word_list[0]
        l=len(w1)
        for w in word_list:
            if len(w)>=l:
                l=len(w)
                w1=w
        return w1
    else:
        return 0

def run():
    word = input('Word: ')
    
    # Initial Mil_Sec
    s = int(round(time() * 1000))
    
    subs = longest_substring(word)
    if subs!=0:
        print(subs)
    else:
        print('No substring possible!')
    # Mil_Secs req 
    print(int(round(time() * 1000)) - s)

if __name__ == '__main__':
    run()

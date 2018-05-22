def chk_palindrome(word):
    flag = True
    if word != word[::-1]:
        flag = False
    return flag

def longest_substring(word):
    if chk_palindrome(word):
        return word
    
    n = len(word)
    for i in range(n-1, -1, -1):
        f = 0
        l = i
        while f<=l:
            if word[f] == word[l-1] and chk_palindrome(word[f:l]):
                w = word[f:l]
                if len(w) == 1:
                    break
                return w
            else:
                f+=1
    for i in range(n):
        f = i
        l = n
        while f<=l:
            if word[f] == word[l-1] and chk_palindrome(word[f:l]):
                w = word[f:l]
                if len(w) == 1:
                    return 0
                return w
            else:
                l-=1

def run():
    word = input('Word: ')
    
    subs = longest_substring(word)
    if subs!=0:
        print(subs)
    else:
        print('No substring possible!')

if __name__ == '__main__':
    run()

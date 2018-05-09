def chk_palindrome(word):
    flag = True
    if word != word[::-1]:
        flag = False
    return flag

def longest_substring(word):
    c = ''
    word_list = ()
    for i in range(len(word)-1):
        c = word[i]
        for j in range(i+1,len(word)):
            if c == word[j]:
                if chk_palindrome(word[i:j+1]):
                    word_list+=(word[i:j+1],)
    
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

word = input('Word: ')
subs = longest_substring(word)
if subs!=0:
    print(longest_substring(word))
else:
    print('No substring possible!')

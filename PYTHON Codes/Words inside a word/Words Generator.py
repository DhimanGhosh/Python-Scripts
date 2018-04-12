import random

english_dictionary = [line.rstrip('\n') for line in open('English Dictionary.txt','r')]

def extract_words(word, length):
    words_list=[]
    if length != 0:
        for i in range(len(word)-length+1):
            words_list.append(word[i:(i+length)])
    return(words_list)

def scramble_word(s):
    n=0
    st=[]
    while n!=len(s):
        st.append(s[n])
        n=n+1
    n=0
    rst=[]
    while n!=len(s):
        rno=random.randint(0,len(s)-1)
        if rst.count(rno)==0:
            rst.append(rno)
            n=n+1
    n=0
    ost=''
    while n!=len(s):
        ost=ost+ st[rst[n]]
        n=n+1
    return(ost)

def factorial(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

def print_words(words_list):
    for l in words_list:
        for k in l:
            if k in english_dictionary or k.upper() in english_dictionary:
                if k.upper() in english_dictionary:
                    print(k.upper())
                else:
                    print(k)

def duplicate_remove_from_list(list1):
    temp_list=[]
    for num in list1:
        if num not in temp_list:
            temp_list.append(num)
    return temp_list

word = input("Word: ")
words_list=[]
for i in range(1,len(word)):
    extracted_words = extract_words(word, i)
    for w in extracted_words:
        for _ in range(factorial(len(w))):
            sw=scramble_word(extracted_words)
            if sw != None:
                words_list.append(sw)

print_words(duplicate_remove_from_list(words_list))



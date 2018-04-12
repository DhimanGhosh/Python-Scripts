english_dictionary = [line.rstrip('\n') for line in open('English Dictionary.txt','r')]

word = input("Word: ")
sorted_word = sorted(word)

words_list=[]
for w in english_dictionary:
    c = 0
    for i in range(len(w)):
        if w[i] in word:
            c+=1
        else:
            break
    if c == len(w):
        words_list.append(w)

for w in words_list:
    flag = True
    sorted_w = sorted(w)
    for i in range(len(sorted_w)):
        if sorted_word[i] != sorted_w[i]:
            flag = False
            break
    if flag:
        print(w)
    else:
        flag = True

'''
for w in words_list:
    print(w)
'''

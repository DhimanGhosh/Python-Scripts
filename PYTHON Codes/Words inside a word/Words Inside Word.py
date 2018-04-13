english_dictionary = [line.rstrip('\n') for line in open('English Dictionary.txt','r')]

word = input("Word: ")
sorted_word = sorted(word)

# Character Frequency in a Word
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

# Possible Dictionary words from Input Word (with Duplicates)
possible_dup_words_list=[]
for w in english_dictionary:
    c = 0
    for i in range(len(w)):
        if w[i] in word:
            c+=1
        else:
            break
    if c == len(w):
        possible_dup_words_list.append(w)

word_char_freq = char_frequency(word) # Frequency of characters in Input Word

# Check character frequency is matching for both words
def chk_freq_match(word2):
    flag = True
    word2_char_freq = char_frequency(word2)
    for k in word_char_freq:
        if k in word2 and word2_char_freq[k]!=word_char_freq[k]:
            flag = False
            break
    return flag

c = 1
# Printing the words list
for w in possible_dup_words_list:
    if chk_freq_match(w) and w!=word:
        print(str(c)+': '+w)
        c+=1

# QUIT
input('Press any key to quit...')

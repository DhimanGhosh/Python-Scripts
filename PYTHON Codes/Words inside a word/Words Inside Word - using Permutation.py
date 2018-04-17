english_dictionary = [line.rstrip('\n') for line in open('English Dictionary.txt','r')]

final_list = []

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

# Check character frequency is matching for both words
def chk_freq_match(word1, word2):
    word_char_freq = char_frequency(word1)
    word2_char_freq = char_frequency(word2)
    flag = True
    for k in word_char_freq:
        if k in word2 and word2_char_freq[k]>word_char_freq[k]:
            flag = False
            break
    return flag

# All Possible Combination of letters in a word
def word_extract(word):
    concat_list = []

    # Character length = 1
    for l in word:
        concat_list.append(l)
    final_list.extend(concat_list)

    # Character length > 1
    counter=1
    while counter!=len(word):
        temp_list = concat_list
        concat_list = []
        for i in range(len(temp_list)):
            for j in range(len(word)):
                w = temp_list[i]
                if temp_list[i][-1]!=word[j]:
                    w+=word[j]
                    concat_list.append(w)
        final_list.extend(concat_list)
        counter+=1

# Printing the List
def print_list(list1, word):
    c = 1
    for w in list1:
        if chk_freq_match(word, w) and w!=word:
            if w.upper() in english_dictionary:
                print(str(c)+': '+w.upper())
                c+=1
            elif w in english_dictionary:
                print(str(c)+': '+w)
                c+=1
    if c==1:
        print('No Possible child word in \''+word+'\'')

def run():
    word = input('Word: ')
    word_extract(word)
    print_list(set(final_list), word)

    # QUIT
    input('Press any key to quit...')


    
if __name__=='__main__':
    run()

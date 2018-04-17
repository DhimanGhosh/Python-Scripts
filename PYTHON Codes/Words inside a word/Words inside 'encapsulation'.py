english_dictionary = [line.rstrip('\n') for line in open('English Dictionary.txt','r')]

words = [line.rstrip('\n') for line in open("Words inside 'encapsulation'.txt",'r')]


print("Words inside: "+words[0][1:-1]+"\n")
words = words[2:]

for i in range(len(words)):
    words[i] = words[i].split('. ')[1]

c=0
for w in words:
    if w in english_dictionary:
        c+=1
        print(w)
print("Count: "+str(c))
input()

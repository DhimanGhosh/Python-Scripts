from List import *

mcc=[line.rstrip('\n') for line in open('mcc.txt','r')]
hunt=[line.rstrip('\n') for line in open('hunt.txt','r')]
os4k=[line.rstrip('\n') for line in open('os4k.txt','r')]
l=len(hunt[0])

'''
Sheet Format
'''
#HUNT
for i in range(len(hunt)):
    hunt[i]=''.join(hunt[i].split(' '))
    #hunt[i]=''.join(hunt[i].split('-'))

#MCC
'''for i in range(len(mcc)):
    mcc[i]=mcc[i][-4:]'''


#Print List
def printArray(num_list):
    for num in num_list:
        print(num)

#Duplicate Removal from a list
def dup_rem_from_list(num_list):
    temp_list=[]
    for num in num_list:
        if num not in temp_list:
            temp_list.append(num)
    return temp_list


#mcc||hunt "Manipulate"
'''#hunt[:-5] + mcc[-5:]
#807002
for i in range(len(hunt)):
    mcc[i]=hunt[i][:-5]+mcc[i][-5:]

c=0
for num in hunt:
    if num in mcc:
        print(num)
        c+=1
h=List(hunt)
print('\nTotal number matched with MCC and HUNT:',c)
if h.total_count()-c==0:
    print('All matched!')
else:
    print('Total number not matched with MCC and HUNT:',h.total_count()-c)'''

#mcc||hunt
c=0
new_num_list=[]
for num in hunt:
    if num in mcc:
        new_num_list.append(num)
        c+=1
print("Numbers in AOIT matched with MCC:")
printArray(dup_rem_from_list(new_num_list))
print('Total Count:',c)

h=List(hunt)
print('\nTot. AOIT:',h.total_count())
m=List(mcc)
print('Tot. MCC:',m.total_count())
print('\nTotal number of AOIT matched with MCC:',c)
if m.total_count()-c==0:
    print('All matched!')
else:
    print('Total number of AOIT not matched with MCC:',h.total_count()-c)
print('Total Remaining MCC device not found in AOIT:',m.total_count()-h.total_count())

'''
Remaining numbers AOIT didn't matched with MCC
'''
rem_hunt=[]
c=0
for num in hunt:
    if num not in new_num_list:
        rem_hunt.append(num)
        c+=1
print("\n\nRemaining numbers in AOIT didn't matched with MCC: ")
printArray(rem_hunt)
print('Total Count:',c)

'''
Excess Numbers in MCC didn't matched with HUNT
'''
new_num_list=[]
c=0
for num in mcc:
    if num not in hunt:
        new_num_list.append(num)
        c+=1
print("\n\nExcess Numbers in MCC didn't matched with HUNT:")
printArray(new_num_list)
print('Total Count:',c)


#mcc||os4k
'''for num in mcc:
    if num[-l1:] in hunt:
        print(num[-l1:])'''

#hunt||os4k
'''c=c1=0
for num in os4k:
    c1+=1
    if num in hunt:
        print(num)
        c+=1
if c==c1:
    print('\nAll matched!')
else:
    print('\nTotal number matched with HUNT and OS4K:',c)'''


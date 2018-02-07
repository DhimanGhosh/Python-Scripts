def append(a,n):
    a1=[0]*(len(a)+1)
    for i in range(len(a)):
        a1[i]=a[i]
    a1[len(a)]=n
    return a1

def extend(a1,a2):
    a=[0]*(len(a1)+len(a2))
    k=0
    while k<len(a):
        if k<len(a1):
            a[k]=a1[k]
        else:
            a[k]=a2[k-len(a2)]
        k+=1
    return a

def insert(a,n,p):
    a1=[0]*(len(a)+1)
    if p>len(a):
        print('List Index Out Of Bounds!')
    elif p==len(a):
        return append(a,n)
    else:
        a1[p]=n
        for i in range(p):
            a1[i]=a[i]
        for i in range(p,len(a)):
            a1[i+1]=a[i]
        return a1

def pop(a):
    if len(a)==0:
        print('Empty List!')
    else:
        a1=[0]*(len(a)-1)
        for i in range(len(a)-1):
            a1[i]=a[i]
        return a1

def pop_pos(a,p):
    if p==(len(a)-1):
        return pop(a)
    else:
        a1=[0]*(len(a)-1)
        for i in range(p):
            a1[i]=a[i]
        for i in range(p,len(a1)):
            a1[i]=a[i+1]
        return a1

def remove(a,n):
    flag=True
    for i in a:
        if i==n:
            flag=False
            break
    if flag:
        print('No such item found!')
    else:
        a1=[0]*(len(a)-1)
        for i in range(len(a)):
            if a[i]==n:
                return pop_pos(a,i)

def clear(a):
    return []

def count(a,n):
    c=0
    for i in a:
        if i==n:
            c+=1
    return c

def reverse(a):
    s=0
    e=len(a)-1
    while s<e:
        a[s],a[e]=a[e],a[s]
        s+=1
        e-=1
    return a

def sort(a,decending=False):#False=Ascending   #True=Decending
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

    if decending:
        return reverse(a)
    else:
        return a

'''a=[1,3,5,7,9]
print(a)
print(append(a,2))'''

'''a1=[1,3,5,7,9]
a2=[2,4,6,8,0]
print(extend(a1,a2))'''

'''a=[1,3,5,7,9]
print(a)
print(insert(a,2,0))'''

'''a=[1,3,5,7,9]
print(a)
print(insert(a,2,len(a)))'''

'''a=[1,3,5,7,9]
print(a)
print(pop(a))'''

'''a=[1,3,5,7,9]
print(a)
print(pop_pos(a,len(a)-1))'''

'''a=[1,3,5,7,9]
print(a)
print(pop_pos(a,2))'''

'''a=[1,3,5,7,9]
print(a)
r=remove(a,5)
if r!=None:
    print(r)

print(clear(a))'''

'''a=[1,3,5,7,9,3,0]
print(count(a,3))'''

'''a=[1,3,5,7,9]
print(a)
print(reverse(a))'''

a=[2,5,1,3,8,7,9]
print(a)
print(sort(a,True))



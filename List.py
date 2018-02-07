class List:
    def __init__(self,a):
        self.__a=a

    def get_a(self):
        return self.__a
    
    def append1(self,n):
        a1=[0]*(len(self.__a)+1)
        for i in range(len(self.__a)):
            a1[i]=self.__a[i]
        a1[len(self.__a)]=n
        return a1
    
    def extend(self,a1,a2):
        a=[0]*(len(a1)+len(a2))
        k=0
        while k<len(a):
            if k<len(a1):
                a[k]=a1[k]
            else:
                a[k]=a2[k-len(a2)]
            k+=1
        return a
    
    def insert(self,a,n,p):
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
    
    def pop(self,a):
        if len(a)==0:
            print('Empty List!')
        else:
            a1=[0]*(len(a)-1)
            for i in range(len(a)-1):
                a1[i]=a[i]
            return a1
    
    def pop_pos(self,a,p):
        if p==(len(a)-1):
            return pop(a)
        else:
            a1=[0]*(len(a)-1)
            for i in range(p):
                a1[i]=a[i]
            for i in range(p,len(a1)):
                a1[i]=a[i+1]
            return a1
    
    def remove(self,a,n):
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
    
    def clear(self,a):
        return []
    
    def count(self,a,n):
        c=0
        for i in a:
            if i==n:
                c+=1
        return c
    
    def reverse(self,a):
        s=0
        e=len(a)-1
        while s<e:
            a[s],a[e]=a[e],a[s]
            s+=1
            e-=1
        return a
    
    def sort(self,a,decending=False):#False=Ascending   #True=Decending
        for i in range(len(a)):
            for j in range(len(a)-i-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
    
        if decending:
            return reverse(a)
        else:
            return a
    

class List:
    def __init__(self,a):
        self.__a=a

    def set_a(self,a):
        self.__a=a

    def get_a(self):
        return self.__a

    def print_list(self):
        for l in self.__a:
            print(l)
    
    def append(self,n):
        a1=[0]*(len(self.__a)+1)
        for i in range(len(self.__a)):
            a1[i]=self.__a[i]
        a1[len(self.__a)]=n
        return a1
    
    def extend(self,a2):
        a=[0]*(len(self.__a)+len(a2))
        k=0
        while k<len(a):
            if k<len(self.__a):
                a[k]=self.__a[k]
            else:
                a[k]=a2[k-len(a2)]
            k+=1
        return a
    
    def insert(self,n,p):
        a1=[0]*(len(self.__a)+1)
        if p>len(self.__a):
            print('List Index Out Of Bounds!')
        elif p==len(self.__a):
            return append(self.__a,n)
        else:
            a1[p]=n
            for i in range(p):
                a1[i]=self.__a[i]
            for i in range(p,len(self.__a)):
                a1[i+1]=self.__a[i]
            return a1
    
    def pop(self):
        if len(self.__a)==0:
            print('Empty List!')
        else:
            a1=[0]*(len(self.__a)-1)
            for i in range(len(self.__a)-1):
                a1[i]=self.__a[i]
            return a1
    
    def pop_pos(self,p):
        if p==(len(self.__a)-1):
            return self.__a.pop()
        else:
            a1=[0]*(len(self.__a)-1)
            for i in range(p):
                a1[i]=self.__a[i]
            for i in range(p,len(a1)):
                a1[i]=self.__a[i+1]
            return a1
    
    def remove(self,n):
        flag=True
        for i in self.__a:
            if i==n:
                flag=False
                break
        if flag:
            print('No such item found!')
        else:
            a1=[0]*(len(self.__a)-1)
            for i in range(len(self.__a)):
                if self.__a[i]==n:
                    return self.__a.pop_pos(i)
    
    def clear(self):
        self.__a=[]
        return self.__a
    
    def count(self,n):
        c=0
        for i in self.__a:
            if i==n:
                c+=1
        return c
    
    def reverse(self):
        s=0
        e=len(self.__a)-1
        while s<e:
            self.__a[s],self.__a[e]=self.__a[e],self.__a[s]
            s+=1
            e-=1
        return self.__a
    
    def sort(self,decending=False):#False=Ascending   #True=Decending
        for i in range(len(self.__a)):
            for j in range(len(self.__a)-i-1):
                if self.__a[j]>self.__a[j+1]:
                    self.__a[j],self.__a[j+1]=self.__a[j+1],self.__a[j]
    
        if decending:
            return reverse(self.__a)
        else:
            return self.__a

    def length(self):
        c=0
        for _ in self.__a:
            c+=1
        return c

    def inside(self, item):
        flag = False
        for item1 in self.__a:
            if item1 == item:
                flag = True
                break
        return flag

    def find_num_pos(self, item):
        for i in range(len(self.__a)):
            if self.__a[i] == item:
                return i
        return None

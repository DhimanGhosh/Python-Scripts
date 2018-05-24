class List:
    #Default Constructor
    def __init__(self):
        self.__a=[]
    
    #Parameterized Constructor
    def __init__(self,a):
        self.__a=a

    #Get List Object
    def get_list(self):
        return self.__a

    #Print content of list
    def print_list(self):
        for l in self.__a:
            print(l)

    #Add an element at the end of the list
    def append(self,item):
        a1=[0]*(len(self.__a)+1)
        for i in range(len(self.__a)):
            a1[i]=self.__a[i]
        a1[len(self.__a)]=item
        self.__a=a1

    #Add elements of another list to the end of current list
    def extend(self,a2):
        a=[0]*(len(self.__a)+len(a2))
        k=0
        while k<len(a):
            if k<len(self.__a):
                a[k]=self.__a[k]
            else:
                a[k]=a2[k-len(a2)]
            k+=1
        self.__a=a

    #Insert an element at any position of a list
    def insert(self,item,p):
        a1=[0]*(len(self.__a)+1)
        if p>len(self.__a):
            print('List Index Out Of Bounds!')
        elif p==len(self.__a):
            return self.append(self.__a,item)
        else:
            a1[p]=item
            for i in range(p):
                a1[i]=self.__a[i]
            for i in range(p,len(self.__a)):
                a1[i+1]=self.__a[i]
            self.__a = a1

    #Removes the last element from the current list
    def pop(self):
        if len(self.__a)==0:
            print('Empty List!')
        else:
            last_elem = self.__a[len(self.__a)-1]
            a1=[0]*(len(self.__a)-1)
            for i in range(len(self.__a)-1):
                a1[i]=self.__a[i]
            self.__a = a1
            return last

    #Removes an element from a specific position of the current list
    def pop_pos(self,p):
        if p==(len(self.__a)-1):
            self.__a.pop()
            return self.__a
        else:
            pos_elem = self.__a[p]
            a1=[0]*(len(self.__a)-1)
            for i in range(p):
                a1[i]=self.__a[i]
            for i in range(p,len(a1)):
                a1[i]=self.__a[i+1]
            self.__a = a1
            return pos_elem

    #Removes an existing item from the current list
    def remove(self,item):
        flag=True
        for i in self.__a:
            if i==item:
                flag=False
                break
        if flag:
            print('No such item found!')
        else:
            a1=[0]*(len(self.__a)-1)
            for i in range(len(self.__a)):
                if self.__a[i]==item:
                    self.__a.pop_pos(i)

    #Clears the content of the current list
    def clear(self):
        self.__a=[]

    #Counts the number of occurence of an item in the current list
    def count(self,item):
        c=0
        for i in self.__a:
            if i==item:
                c+=1
        return c

    #Reverses the current list
    def reverse(self):
        s=0
        e=len(self.__a)-1
        while s<e:
            self.__a[s],self.__a[e]=self.__a[e],self.__a[s]
            s+=1
            e-=1
        return self.__a

    #Sort the elements of the current list (Bubble Sort)
    def sort(self,decending=False):#False=Ascending   #True=Decending
        for i in range(len(self.__a)):
            for j in range(len(self.__a)-i-1):
                if self.__a[j]>self.__a[j+1]:
                    self.__a[j],self.__a[j+1]=self.__a[j+1],self.__a[j]
    
        if decending:
            self.__a.reverse()

    #Counts the total length of the current list
    def length(self):
        c=0
        for _ in self.__a:
            c+=1
        return c

    #Checks if an item is present in the current list
    def inside(self, item):
        flag = False
        for item1 in self.__a:
            if item1 == item:
                flag = True
                break
        return flag

    #Finds in which position an item is present in the current list
    def find_num_pos(self, item):
        for i in range(len(self.__a)):
            if self.__a[i] == item:
                return i
        return None

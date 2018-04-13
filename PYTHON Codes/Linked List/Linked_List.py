class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        temp=Node(data)
        if self.__head==self.__tail==None:
            self.__head=self.__tail=temp
        else:
            p=self.__head
            while p.get_next()!=None:
                p=p.get_next()
            p.set_next(temp)
            self.__tail=p
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
        if self.__head==self.__tail==None:
            print("No Items to Display!")
        else:
            p=self.__head
            while p!=None:
                print(p.get_data())
                p=p.get_next()
            print()
        #Remove pass and copy the code you had written to display the element(s).
    
    def find_node(self,data):
        if self.__head==self.__tail==None:
            print('List is empty!')
        else:
            p=self.__head
            while p!=None:
                if p.get_data()==data:
                    return True
                p=p.get_next()
            return False
        #Remove pass and copy the code you had written to find the node containing the element.
    
    def insert(self,data,data_before):
        temp=Node(data)
        if self.__head==self.__tail==None:
            temp1=Node(data_before)
            self.__head=temp1
            temp1.set_next(temp)
            self.__tail=temp
        else:
            p=self.__head
            while p.get_data()!=data_before:
                if p.get_data()==data_before:
                    temp.set_next(p.get_next())
                    p.set_next(temp)
                    print('{} added'.format(data))
                    break
                elif p.get_next()==None and p.get_data()!=data_before:
                    print('{} not found!'.format(data_before))
                    break
                p=p.get_next()
        #Remove pass and write the logic to insert an element.

list1=LinkedList()
#Add all the required element(s)
#Insert the element in the required position
list1.add('Salt')
list1.add('Sugar')
list1.add('Tea')
list1.add('Coffee')
list1.display()

list1.insert('NewItem','Sugar')
list1.display()

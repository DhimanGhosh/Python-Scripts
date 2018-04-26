'''
*****Telephone Directory*****
A Simple Console Application (using List)

New Feature/s:
1. Store Telephone Numbers in a text file

Future Feature's:
1. Can Search with some initial characters
2. Fast Accessable (using Trie)
'''

class Tel_Dir(object):
    def __init__(self):
        f = open('tel_dir.txt','w')
        f.write('*****TELEPHONE DIRECTORY***\n')
        f.write('Name\t\t\tPhone Number\n')
        f.write('****\t\t\t************\n')
        self.name_list=[]
        self.num_list=[]
        self.dict1={}

        self.n=input("Enter the number of contacts : ")
        for i in range(int(self.n)):
            self.name = input('Enter your Name: ')
            self.num = input('Enter your Phone Number: ')
            if len(self.name)<=2:
                f.write(self.name+'\t\t\t\t'+self.num+'\n')
            elif len(self.name)<=6:
                f.write(self.name+'\t\t\t'+self.num+'\n')
            elif len(self.name)<12:
                f.write(self.name+'\t\t'+self.num+'\n')
            elif len(self.name)>=12:
                f.write(self.name+'\t'+self.num+'\n')
            self.name_list.append(self.name)
            self.num_list.append(self.num)
            self.dict1 = dict(zip(self.name_list, self.num_list)) #to convert two list into dictionary
        self.print_dict()
        f.close()
    
    def print_dict(self):
        print('\n*****TELEPHONE DIRECTORY***')
        print('Name\t\t\tPhone Number')
        print('****\t\t\t************')
        for key in self.dict1:
            print(key+'\t\t'+self.dict1[key])

    def choose(self):
        print("""
\t1:Add a contact
\t2:Search a contact
\t3:Delete a contact
\t4:Update a contact
\t5:View directory
\t6:Exit
    """)
        choice=input("\tEnter your choice: ")
        return int(choice)

    def add(self,name,num):
        f = open('tel_dir.txt','a')
        if len(self.name)<=2:
            f.write(self.name+'\t\t\t\t'+self.num+'\n')
        elif len(self.name)<=6:
            f.write(self.name+'\t\t\t'+self.num+'\n')
        elif len(name)<12:
            f.write(name+'\t\t'+num+'\n')
        elif len(name)>=12:
            f.write(name+'\t'+num+'\n')
        f.close()
        self.dict1[name] = num
        print("\'"+name+"\' added...")
        self.print_dict()

    def search(self,name):
        temp = None
        for n in self.dict1:
            if n==name:
                temp = n
                break
        if temp!=None:
            return self.dict1[temp]
        return temp

    def delete(self,name):
        if self.search(name)!=None:
            del self.dict1[name]
            print("\'"+name+"\' deleted...")
            self.print_dict()
        else:
            print("\'"+name+"\' does not exist!")

    def update(self):
        name = input("Enter the name which you want to update: ")
        if self.search(name)!=None:
            num = input("Enter the new number: ")
            self.dict1[name] = num
            print("\'"+name+"\' updated...")
            self.print_dict()
        else:
            print("\'"+name+"\' does not exist!")


def driver():
    t = Tel_Dir()

    while True:
        choice = t.choose()
        if (choice == 1):
            name = input("Enter the new name you want to add: ")
            num = input("Enter the number: ")
            t.add(name, num)
     
        elif (choice == 2):
            name = input("Enter the name whose number is to be found: ")
            res = t.search(name)
            if res!=None:
                print("\'"+name+"\' found...\n")
                print(name+': '+res)
            else:
                print("\'"+name+"\' does not exist!")
            
        elif (choice == 3):
            name = input("Enter the name you want to delete: ")
            t.delete(name)
            
        elif (choice == 4):
            t.update()

        elif (choice == 5):
            t.print_dict()

        elif (choice == 6):
            break

if __name__ == '__main__':
    driver()
    #os.remove('tel_dir.txt')

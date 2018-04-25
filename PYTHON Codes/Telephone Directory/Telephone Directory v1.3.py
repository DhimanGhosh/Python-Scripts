'''
*****Telephone Directory*****
A Simple Console Application (using Trie)

New Feature/s:
1. Dial (using name)
2. Speed Dial

Future Feature/s:
1. Dial (using number present in directory)
2. While dialing new number (add to Telephone Directory)
'''

from Trie import Trie
class Tel_Dir(object):
    def __init__(self):
        f = open('tel_dir.txt','w')
        f.write('*****TELEPHONE DIRECTORY***\n')
        f.write('Name\t\t\tPhone Number\n')
        f.write('****\t\t\t************\n')
        self.name_list=[]
        self.num_list=[]
        self.dict1={}
        self.trie = Trie()
        self.speed_dial_list = [None]*9

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

    def dial_with_name(self,name):
        pass
    
    def assign_speed_dial(self,index,num):
        pass
    
    def sort_dict(self,dict1):
        sorted_dict_list = sorted(dict1.items())
        temp_dict = {}
        for dict_item in sorted_dict_list:
            temp_dict[dict_item[0]] = dict_item[1]
        return temp_dict
    
    def print_dict(self):
        print('\n*****TELEPHONE DIRECTORY***')
        print('Name\t\t\tPhone Number')
        print('****\t\t\t************')
        for key in self.dict1:
            self.trie.insert(key)
            print(key+'\t\t'+self.dict1[key])

    def choose(self):
        print("""
\t1:Add a contact
\t2:Search a contact
\t3:Delete a contact
\t4:Update a contact
\t5:Search with starting characters
\t6:View directory
\t7:Dial (using name ONLY)
\t8:Assign Speed dial
\t9:Exit
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
        self.trie.insert(name)
        print("\'"+name+"\' added...")
        self.print_dict()

    def search(self,name):
        if self.trie.search(name)==1:
            return self.dict1[name]
        return None

    def search_by_chrs(self,str1):
        sorted_directory = self.sort_dict(self.dict1)
        length = len(str1)
        c = 0
        for key in sorted_directory:
            if key[:length] == str1:
                print(key+'\t\t'+sorted_directory[key])
                c+=1
        if c==0:
            print("Name starting with \'"+str1+"\' does not exist!")

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

# Driver
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
            chrs = input('Some initial characters: ')
            t.search_by_chrs(chrs)

        elif (choice == 6):
            t.print_dict()

        elif (choice == 7):
            '''
            part -> take as input
            if more than 1 present let user choose using 1/2/3/.... (listed numerically)
            name=result
            dial_with_name(name)
            '''

        elif (choice == 8):
            '''
            Assign from 1-9:
            e.g.,
            assign_speed_dial(1,search(name))
            '''

        elif (choice == 9):
            break

if __name__ == '__main__':
    driver()

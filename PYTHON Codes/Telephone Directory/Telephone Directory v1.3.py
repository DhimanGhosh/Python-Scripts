'''
*****Telephone Directory*****
A Simple Console Application (using Trie)

New Feature/s:
1. Dial (using name/initials)
2. Speed Dial

Future Feature/s:
1. Dial (using number present in directory)
2. While dialing new number (add to Telephone Directory)
'''

from Trie import Trie
import time
class Tel_Dir(object):

    # Constructor
    def __init__(self):
        f = open('tel_dir.txt','w')
        f.write('*****TELEPHONE DIRECTORY***\n')
        f.write('Name\t\t\tPhone Number\n')
        f.write('****\t\t\t************\n')
        self.dict1={}
        self.trie = Trie()
        self.__speed_dial_list = [None]*9

        self.n=input("Enter the number of contacts : ")
        for _ in range(int(self.n)):
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
            self.dict1[self.name] = self.num
        self.print_dict()
        f.close()

    # Menu for choosing within options
    def choose(self):
        print("""
\t1:Add a contact
\t2:Search a contact
\t3:Delete a contact
\t4:Update a contact
\t5:Search with starting characters
\t6:View directory
\t7:Dial
\t8:Assign Speed dial
\t9:Exit
    """)
        choice=input("\tEnter your choice: ")
        return int(choice)

    # Add a new contact to Telephone Directory
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

    # Search for a contact using full name in Telephone Directory
    def search(self,name):
        if self.trie.search(name)==1:
            return self.dict1[name]
        return None

    # Delete an existing name from Telephone Directory
    def delete(self,name):
        if self.search(name)!=None:
            del self.dict1[name]
            print("\'"+name+"\' deleted...")
            self.print_dict()
        else:
            print("\'"+name+"\' does not exist!")

    # Update the Name / Phone Number of a perticular contact in Telephone Directory
    def update(self):
        name = input("Enter the name which you want to update: ")
        if self.search(name)!=None:
            num = input("Enter the new number: ")
            self.dict1[name] = num
            print("\'"+name+"\' updated...")
            self.print_dict()
        else:
            print("\'"+name+"\' does not exist!")

    ### Helper (Private) Method for sorting dictionary retaining values
    def __sort_dict(self,dict1):
        sorted_dict_list = sorted(dict1.items())
        temp_dict = {}
        for dict_item in sorted_dict_list:
            temp_dict[dict_item[0]] = dict_item[1]
        return temp_dict

    # Search for a contact using some initial characters in Telephone Directory
    def search_by_chrs(self,str1):
        sorted_directory = self.__sort_dict(self.dict1)
        length = len(str1)
        temp_dict = {}
        c = 0
        for key in sorted_directory:
            if key[:length] == str1:
                print(key+'\t\t'+sorted_directory[key])
                c+=1
                temp_dict[key] = sorted_directory[key]
        if c!=0:
            return temp_dict
        print("Name starting with \'"+str1+"\' does not exist!")
        return None

    # Print the content of Telephone Directory
    def print_dict(self):
        print('\n*****TELEPHONE DIRECTORY***')
        print('Name\t\t\tPhone Number')
        print('****\t\t\t************')
        for key in self.dict1:
            self.trie.insert(key)
            print(key+'\t\t'+self.dict1[key])

    ### (Helper) Retrieve Fullname/Number corresponding to an input name/initials (0/<skip>: FullName, 1:Number)
    def __get_fullname_num_from_name_initials(self,name_chrs,f_n=0):
        temp_dict = self.search_by_chrs(name_chrs)
        if temp_dict!=None:
            if len(temp_dict) > 1:
                print('Choose which one to dial: ')
                for i,key in enumerate(temp_dict.keys()):
                    print(str(i+1)+': '+key+'\t'+temp_dict[key])
                ch = input('Option: ')
                for i,key in enumerate(temp_dict.keys()):
                    if i==(int(ch)-1):
                        if f_n==1:
                            return temp_dict[key]
                        return key
            else:
                if f_n==1:
                    name,num = temp_dict.popitem()
                    return num
                return temp_dict.popitem()
    
    ### (Helper/Dialer) Dial with an existing name in Telephone Directory
    def __dial_with_name_chrs(self,name):
        print('Dialing... '+str(name)+' ('+str(self.dict1[name])+')')
        time.sleep(5)
        print('\n***Connected***\nHave a nice conversation\n')
        input('Press any key to hang-up...')

    # Dial with an existing name in Telephone Directory
    def dial_with_name_chrs(self,name_chrs):
        if self.search(name_chrs) != None:
            self.__dial_with_name_chrs(name_chrs)
        else:
            name = self.__get_fullname_num_from_name_initials(name_chrs)
            self.__dial_with_name_chrs(name)
            

    # Assign speed dial from 1-9 with an existing name in Telephone Directory
    def assign_speed_dial(self,index,name):
        num = self.__get_fullname_num_from_name_initials(name,1)
        if self.__speed_dial_list[index-1]!=None:
            self.__speed_dial_list[index-1] = num
            print(str(num)+' is registered at index '+str(index-1))
        else:
            choice = input('WARNING! Do you want to replace the previously assigned number? (Y/N)')
            if choice=='Y' or choice=='y':
                self.__speed_dial_list[index-1] = num
                print(str(num)+' is registered at index '+str(index-1))
            elif choice=='N' or choice=='n':
                print(str(self.__speed_dial_list[index-1])+' is being retained at index '+str(index-1))

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
            name_chrs = input('Name / Some initial characters: ')
            t.dial_with_name_chrs(name_chrs)

        elif (choice == 8):
            print('''
\tYou can assign any 9 numbers to speed-dial from 1-9:
Now you can proceed:''')
            time.sleep(2)

            index = input('Index number to assign: ')
            name = input('Name/ Some initial characters: ')
            t.assign_speed_dial(index,name)
            '''
            Assign from 1-9:
            e.g.,
            assign_speed_dial(1,search(name))
            '''

        elif (choice == 9):
            break

if __name__ == '__main__':
    driver()

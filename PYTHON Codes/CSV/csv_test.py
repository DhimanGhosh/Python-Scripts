file_name = 'test.csv'
f = open(file_name, 'w')

headers = 'Name, E-mail, DOB\n'
f.write(headers)

names = ['Dhiman', 'Anirban', 'Amit', 'Keya']
emails = ['abc@gmail.com',
         'xyz@gmail.com',
         'pqr@gmail.com',
         'help@gmail.com']
DOB = ['05/12/1993',
       '12/03/1965',
       '26/09/1989',
       '12/06/1991']

for i in range(len(names)):
    f.write(names[i] + "," +
            emails[i] + "," +
            DOB[i] + "\n")
f.close()

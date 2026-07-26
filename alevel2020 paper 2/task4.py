import datetime, sqlite3
class Person:
    def __init__(self, name, DoB):
        self.full_name = name
        self.date_of_birth = DoB #YYYY-MM-DD
        return
    
        
        
        
    def is_adult(self):
        today = datetime.date.today() #datetime
        num_equiv = ''
        for i in str(today):
            if i.isdigit():
                num_equiv = num_equiv + i
                
            else:
                pass
        
        num_equiv = int(num_equiv)
        
        
        bday = ''
        
        for i in self.date_of_birth:
            if i .isdigit():
                bday = bday + i
            else:
                pass
            
            
        bday = int(bday)
        
        
        check = num_equiv - bday
        
        
        if check >= 180000:
            return True
        else:
            return False
            
        
        
    def screen_name(self):
        name = ''
        
        for i in self.full_name:
            if i.isalpha():
                name = name + i
            else:
                pass
            
            
        bday = self.date_of_birth
        month = bday[5:7]
        day = bday[8:]
        
        screenname = name + month + day
        
        
        return screenname
    
    
P = Person('John Tan', '2000-06-01')

print(P.screen_name())

















#task 4.2

#creating the subclass
class Student(Person):
    def __init__(self, name, DoB):
        super().__init__(name, DoB)   # call Person’s __init__
        return

    def is_adult(self):
        return False


    


    
        

class Staff(Person):

    def __init__(self, name, DoB):
        super().__init__(name, DoB)
        return


    def is_adult(self):
        return True


#getting all the data from the people.txt and then inserting into classes


openfile = open('people.txt', 'r')
data = openfile.readlines()
openfile.close()


List_of_objects = []

for i in data:
    i = i.strip()
    arr = i.split(',')

    name, dob, cLass = arr[0],arr[1], arr[2]

    if cLass == 'Person':
        obj = Person(name, dob)
        
        
    elif cLass == 'Staff':
        obj = Staff(name, dob)
    elif cLass == 'Student':
        obj = Student(name, dob)

    List_of_objects.append(obj)


        

    

#print(List_of_objects)









#creating the database

connection = sqlite3.connect('school.db')
connection.execute('DROP TABLE IF EXISTS People') #dropping People table first


openfile = open('task4_1.sql')
data = openfile.read() #.read() is enough to get all the stuff
openfile.close()

connection.executescript(data)#execute script is how to create using sql file

connection.commit()



#inserting into db

for i in List_of_objects:
    FullName = i.full_name #attributes dont need()
    DateOfBirth = i.date_of_birth
    ScreenName = i.screen_name() #method/func need ()
    IsAdult = i.is_adult()

    if IsAdult == True:
        IsAdult = 1 # 1 measn true

    else:
        IsAdult = 0


    connection.execute('INSERT INTO People(FullName, DateOfBirth, ScreenName, IsAdult)  VALUES(?, ?, ?, ?)', (FullName, DateOfBirth, ScreenName, IsAdult))
connection.commit()


#close connection after finishing everything
connection.close()


#DONE
    
    







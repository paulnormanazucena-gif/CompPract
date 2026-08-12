import sqlite3
from flask import *

#getting values
def drop_tables():
    connection = sqlite3.connect("library.db") #the entire db
    #execute is to run sql code
    connection.execute("DROP TABLE IF EXISTS Loans")    
    connection.execute("DROP TABLE IF EXISTS Users")    
    connection.execute("DROP TABLE IF EXISTS Books") 
    
    connection.commit()#finalises the changes
    connection.close() #always needs to close
    return

def create_tables():
    
    connection = sqlite3.connect("library.db")
    
    #need create those without foreign key first
    
    #creating the Books tables
    connection.execute("""
        CREATE TABLE 'Books' (
        'ISBN' TEXT NOT NULL,
        'Title' TEXT,
        'Damaged' BOOLEAN,
        PRIMARY KEY('ISBN')
    );""")
    
    
    connection.execute("""
        CREATE TABLE 'Users' (
        'Name' TEXT NOT NULL,
        'Gender' TEXT,
        PRIMARY KEY('Name')
    );
    """)
    
    #this is important shows how to do foreign key
    
    connection.execute("""
    CREATE TABLE 'Loans' (
    'userID' TEXT,
    'ISBN' TEXT,
    'date_loaned' TEXT NOT NULL,
    PRIMARY KEY('userID','ISBN'),
    FOREIGN KEY ('userID') REFERENCES 'Users'('Name'),
    FOREIGN KEY ('ISBN') REFERENCES 'Books'('ISBN')
    );
    """)
    

#main program
drop_tables()
create_tables()


#inserting into user

openfile = open('user.txt', 'r')
data = openfile.readlines()
USERS = [] # all the data here
for i in range(1, len(data)):
    cleared = data[i][:-1]
    
    array1d = []
    name, gender = cleared.split(',')
    array1d.append(name)
    array1d.append(gender)
    
    USERS.append(array1d)
    
openfile.close()
    
    

#inserting in to Book= ops
openfile = open('book (1).txt', 'r')
data = openfile.readlines()
openfile.close()
BOOKS = []#

for i in range(1, len(data)):
    cleared = data[i][:-1]
    
    array1d = []
    ISBN, title, damaged =cleared.split(',')
    
    
    if damaged == 'True':
        damage = 1
        
    else:
        damage = 0
        
    array1d.append(ISBN)
    array1d.append(title)
    array1d.append(damage)
    
    BOOKS.append(array1d)






#inserting into Loans
openfile = open('loan.txt', 'r')
data = openfile.readlines()
openfile.close()
LOANS = []#
for i in range(1, len(data)):
    cleared = data[i][:-1]
    
    array1d = []
    userID, ISBN, date_loaned =cleared.split(',')
    array1d.append(userID)
    array1d.append(ISBN)
    array1d.append(date_loaned)
    
    LOANS.append(array1d)

#INSERTING

connection = sqlite3.connect('library.db')

#books

for i in BOOKS:
    
    connection.execute('INSERT INTO Books (ISBN, Title, Damaged) VALUES (?,?,?)', (i[0], i[1], i[2]) )

for i in USERS:
    connection.execute('INSERT INTO Users (Name, Gender) VALUES (?,?)', (i[0], i[1]))

for i in LOANS:
    connection.execute('INSERT INTO Loans(userID, ISBN, date_loaned) VALUES (?,?,?)', (i[0],i[1],i[2]))
    
connection.commit()
connection.close()

print('inserted')

connection = sqlite3.connect('library.db')

data = connection.execute('SELECT * FROM Loans ')
results = data.fetchall()
connection.close()  


#



app = Flask(__name__, template_folder=r"C:\Users\pauln\OneDrive\Desktop\WEB APP\templates")
@app.route('/')
def home():
    connection = sqlite3.connect('library.db')

    data = connection.execute('SELECT * FROM Loans ')
    results = data.fetchall()
    connection.close()

    
    return render_template('Index.html', Loans = results)



@app.route('/search', methods = ["POST"])
def search():
    data = request.form
    user = data['username']
    isbn = data['ISBN'] 
    date_loaned = data['dateloaned']


    connection = sqlite3.connect('library.db')
    check = connection.execute(" SELECT * FROM Loans WHERE Loans.ISBN = ?", (isbn,))
    if len(check.fetchall()) >= 1:
        return render_template('NOTapproved.html')
    else:
        pass


    connection.execute(' INSERT INTO Loans(userID, ISBN, date_loaned) VALUES (?,?,?)', (user, isbn, date_loaned))

    connection.commit()
    connection.close()

    return render_template('approved.html', user = user, isbn = isbn, date_loaned = date_loaned)

@app.route('/goback', methods = ["POST"])
def goback():
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True)

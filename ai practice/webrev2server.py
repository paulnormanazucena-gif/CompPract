from flask import *
import sqlite3
def createtables():
    connection = sqlite3.connect('ITLoan.db')

    connection.execute("""
    CREATE TABLE student (
	studentID	TEXT,
	name	TEXT,
	phoneNo	TEXT,
	PRIMARY KEY(studentID)
    );""")

    connection.execute("""
    CREATE TABLE category (
	categoryID INTEGER PRIMARY KEY AUTOINCREMENT,
	categoryName	TEXT
	
    );
    """)

    connection.execute("""
    CREATE TABLE equipment (
	equipID	INTEGER PRIMARY KEY AUTOINCREMENT,
	categoryID	TEXT,
	equipName	TEXT,
	brand	TEXT,
	availableQty	INTEGER,
	FOREIGN KEY(categoryID) REFERENCES category(categoryID)
    );""")

    connection.execute("""
    CREATE TABLE loanRecord (
	studentID	TEXT,
	equipID	INTEGER,
	loanDate	TEXT,
	returnDate	TEXT,
	availableQty	INTEGER,
	PRIMARY KEY(studentID,equipID),
	FOREIGN KEY(studentID) REFERENCES student(studentID),
	FOREIGN KEY(equipID) REFERENCES equipment(equipID)
    );""")

    connection.commit()
    connection.close()
    return

def droptables():
    connection = sqlite3.connect('ITLoan.db')
    connection.execute("DROP TABLE IF EXISTS loanRecord")
    connection.execute("DROP TABLE IF EXISTS equipment")
    connection.execute("DROP TABLE IF EXISTS category")
    connection.execute("DROP TABLE IF EXISTS student")
    connection.commit()
    connection.close()
    return

def getfile(filename):
    openfile = open(filename, 'r')
    data = openfile.readlines()
    openfile.close()
    return data

#main program
droptables()
createtables()


#inserting sutdents
connection = sqlite3.connect('ITLoan.db')


data = getfile('STUDENT.txt')
for i in range(len(data) -1):
    data[i] = data[i][:-1]
#
nrics = []
studids =[]


for i in data:
    nric, name, number = i.split(',')

    first4 = ''
    for i in name:
        if len(first4) == 4:
            break


        
        if i.isalpha():
            first4 = first4 + i
        else:
            pass

    studid = first4.upper() + number[4:]
    nrics.append(nric)
    studids.append(studid)

    connection.execute("""
    INSERT INTO student(studentID, name, phoneNo) VALUES (?,?,?)""",
    (studid, name, number))

#print(connection.execute(" SELECT * FROM student").fetchall())

data = getfile('CATEGORY.txt')

for i in range(len(data) -1):
    data[i] = data[i][:-1]

for i in data:
    catID, catname = i.split(',')
    connection.execute("INSERT INTO category(categoryID, categoryName) VALUES (?,?)",
    (catID, catname))
    
#print(connection.execute(" SELECT * FROM category").fetchall())
    
data = getfile('EQUIPMENT.txt')

for i in range(len(data) -1):
    data[i] = data[i][:-1]

for i in data:
    equipID, categoryID, equipName, brand, QTY = i.split(',')
    connection.execute('INSERT INTO equipment(equipID, categoryID, equipName, brand, availableQty) VALUES (?,?,?,?,?)',
    (equipID, categoryID, equipName, brand, QTY))
#print(connection.execute(" SELECT * FROM equipment").fetchall())
    

#loan
data = getfile('LOANRECORD.txt')


for i in range(len(data) -1):
    data[i] = data[i][:-1]

#5 values
for i in data:
    NRIC, eqid, loandate, returndate, qty = i.split(',')

    index = nrics.index(NRIC)
    studid = studids[index]
   
    connection.execute("INSERT INTO loanRecord(studentID, equipID, loanDate, returnDate, availableQty) VALUES (?,?,?,?,?)",
   (studid, eqid, loandate, returndate, qty  ))



  
    



connection.commit()
connection.close()

#SELECT  category.categoryID, equipment.equipName, equipment.brand
#FROM equipment, category
#WHERE category.categoryName = 'Laptops' and category.categoryID = equipment.categoryID
    
#webapp
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods = ["POST"])
def calculate():
    data = request.form
    studid = data['studid']
    date = data['date']


    #want total items, so find the data when stude =  and loan date =
    #find all the quatntities, then add up
    connection = sqlite3.connect('ITLoan.db')
    loans = connection.execute("""
    SELECT loanRecord.availableQty
    FROM loanRecord
    WHERE loanRecord.studentID = ? and loanRecord.loanDate = ?
    """, (studid, date)).fetchall() #.fetchall() occurs outside of the connection.execute
    total = 0
    for i in loans:
        total += int(i[0])
        
    return render_template('results.html', loans = total)

@app.route('/goback', methods = ["POST"])
def goback():
    return redirect('/')

if __name__ == '__main__':
    
    app.run(host = '127.0.0.1', port = 3000, debug = True)


#DO NOT FORGET THE <TABLE>



















    

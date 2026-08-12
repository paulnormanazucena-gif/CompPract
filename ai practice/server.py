import sqlite3
from flask import *


def createtables():
    
    connection = sqlite3.connect('subject_grades.db')
    connection.execute("""
    CREATE TABLE student (
            studentID	TEXT,
            name	TEXT,
            formClass	TEXT,
            PRIMARY KEY(studentID)
    );
    """)
    connection.execute("""
    CREATE TABLE subject (
            subjCode	TEXT,
            subjName	TEXT,
            PRIMARY KEY(subjCode)
    );
    """)
    connection.execute("""
    CREATE TABLE grade_record (
            recordID	INTEGER PRIMARY KEY AUTOINCREMENT,
            studentID	TEXT,
            subjCode	TEXT,
            grade	TEXT,
            FOREIGN KEY(subjCode) REFERENCES subject(subjCode),
            FOREIGN KEY(studentID) REFERENCES student(studentID)
    );

    """)

    connection.commit()
    connection.close()
    return

def droptables():
    connection = sqlite3.connect('subject_grades.db')

    connection.execute("DROP TABLE IF EXISTS grade_record")
    connection.execute("DROP TABLE IF EXISTS subject")
    connection.execute("DROP TABLE IF EXISTS student")

    
    connection.commit()
    connection.close()
    return


#creating and delerting table
droptables()
createtables()

connection = sqlite3.connect('subject_grades.db')

#inserting

openfile = open('STUDENT.txt', 'r')
data = openfile.readlines()
openfile.close()

for i in range(len(data)-1): #clean
    data[i] = data[i][:-1]



for i in data:
    studid, name, classs = i.split(',')
    connection.execute('INSERT INTO student(studentID, name, formClass) VALUES (?,?,?)', (studid, name, classs))

#print(connection.execute("SELECT * FROM student").fetchall())

openfile = open('SUBJECT.txt', 'r')
data = openfile.readlines()
openfile.close()

for i in range(len(data)-1):
    data[i] = data[i][:-1]

for i in data:
    
    code, name = i.split(',')
    connection.execute("INSERT INTO subject(subjCode, subjName) VALUES (?,?)", (code, name))
#woirks


openfile = open('GRADE.txt', 'r')
data = openfile.readlines()
openfile.close()

#studi, suvjcode, grade
for i in range(len(data)-1):
    data[i] = data[i][:-1]


for i in data:
    studid, subjcode, grade = i.split(',')
    connection.execute("INSERT INTO grade_record(studentID,subjCode,grade) VALUES (?,?,?)", (studid, subjcode, grade))
#print(connection.execute("SELECT * FROM grade_record").fetchall())
connection.commit()
connection.close()
#all inserted done


#task 2.3

#SELECT student.name, subject.subjName, grade_record.grade
#FROM student, subject, grade_record
#WHERE grade_record.grade = 'A' and student.studentID = grade_record.studentID and grade_record.subjCode = subject.subjCode
#web app
app = Flask(__name__)

@app.route('/')
def home():
    connection = sqlite3.connect("subject_grades.db")
    results = connection.execute("""
            SELECT student.name, student.formClass, subject.subjName, grade_record.grade
            FROM subject, student, grade_record
            WHERE student.studentID = grade_record.studentID and subject.subjCode = grade_record.subjCode""").fetchall()


    return render_template('index.html', results = results)


@app.route('/search', methods = ["POST"])
def search():
    data = request.form
    category = data
    value = data['value']

    connection = sqlite3.connect('subject_grades.db')
    results = connection.execute("""
    SELECT student.name, student.formClass, subject.subjName, grade_record.grade
    FROM subject, student, grade_record
    WHERE student.studentID = grade_record.studentID and subject.subjCode = grade_record.subjCode and student.name = ?
    """, (value,)).fetchall()

    connection.close()

    

    

    return render_template('results.html', results = results)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8000, debug = True)










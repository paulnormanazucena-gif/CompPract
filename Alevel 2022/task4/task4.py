from flask import *
import sqlite3




app = Flask(__name__)

@app.route('/')
def home():
    connection = sqlite3.connect('LIBRARY.db')
    List = connection.execute("""
    SELECT Member.FamilyName, Member.GivenName, Book.Title
    FROM Member, Book, Loan
    WHERE Loan.Returned = 0 and Loan.MemberNumber = Member.MemberNumber and Loan.BookID = Book.BookID
    """).fetchall()
    connection.close()


    
    return render_template('index.html', List = List)




if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=5000, debug = True)
    

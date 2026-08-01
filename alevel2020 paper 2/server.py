from flask import *
import sqlite3




#starting webapp

app = Flask(__name__)

@app.route('/')
def home():
    #start connection
    connection = sqlite3.connect('school.db')


    thing = connection.execute('SELECT * FROM People').fetchall()
    #end connection whene evrything is finished
    connection.close()
    return render_template('index.html', thing = thing)


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True)

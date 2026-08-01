import sqlite3
from flask import *



#db browser test
connection = sqlite3.connect('Task4.db')
documents = connection.execute("""
SELECT competitor.name, scores.score
FROM competitor, scores
WHERE competitor.id = scores.id and scores.round = ?
""", (1,)).fetchall()

connection = sqlite3.connect('Task4.db')
documents = connection.execute("""
SELECT competitor.name, scores.round, scores.score
FROM competitor
JOIN scores ON competitor.id = scores.id
ORDER BY competitor.name ASC, scores.round ASC;
""").fetchall()
#for i in documents:
    #print(i)


connection  = sqlite3.connect('Task4.db')
scores = connection.execute("SELECT * FROM scores").fetchall()
competitors = connection.execute("SELECT * FROM competitor").fetchall()

pairs = []

for i in competitors:
    name = i[1]
    ID = i[0]
    total = 0
    count = 0
    for score in scores:
        if score[0] == ID:
            count +=1
            total = total + score[2]

 
    mean =  total / count
    pair = (name, round(mean, 1))
    pairs.append(pair)










#web app


app = Flask(__name__) #forgot

@app.route('/') #forgot
def home():
    
    
    return render_template('index.html')


@app.route('/options', methods = ['POST']) #remember
def options():
    data = request.form #forgot

    option = data['option']
    

    if option == '1' or option == '2' or option == '3':
        r = option
        r= int(r)


        connection = sqlite3.connect('Task4.db') 
        documents = connection.execute("""
        SELECT competitor.name, scores.score
        FROM competitor, scores
        WHERE competitor.id = scores.id and scores.round = ?
        """, (r,)).fetchall()
        connection.close()

        


        return render_template('round_results.html', r = r, documents = documents)


        

    


    elif option == '4': #mean scores

        connection  = sqlite3.connect('Task4.db')
        scores = connection.execute("SELECT * FROM scores").fetchall()
        competitors = connection.execute("SELECT * FROM competitor").fetchall()

        pairs = []

        for i in competitors:
            name = i[1]
            ID = i[0]
            total = 0
            count = 0
            for score in scores:
                if score[0] == ID:
                    count +=1
                    total = total + score[2]

 
            mean =  total / count
            pair = (name, round(mean, 1))
            pairs.append(pair)
        List = pairs
        connection.close()




        return render_template('mean.html', List = List)

                


    elif option == '5': #qualifiers
        connection  = sqlite3.connect('Task4.db')
        scores = connection.execute("SELECT * FROM scores").fetchall()
        competitors = connection.execute("SELECT * FROM competitor").fetchall()

        pairs = []

        for i in competitors:
            name = i[1]
            ID = i[0]
            total = 0
            
            for score in scores:
                if score[0] == ID:
                    
                    total = total + score[2]

 
            
            pair = [name, total]
            pairs.append(pair)

        for i in pairs:
            if i[1] > 250:
                i.append('Qualified')
            else:
                i.append('Not Qualified')
        connection.close()

        List = pairs

        return render_template('qualified.html', List = List)

        

    
        


if __name__ == '__main__': #forgot
    app.run(host= '127.0.0.1', port = 5000, debug = True) #cannot have any space.?

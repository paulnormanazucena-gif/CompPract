from flask import *

openfile = open('deccompressedimage.txt','r')
data = openfile.readlines()
openfile.close()

List = []
for i in range(0, len(data[0]), 3):
    
    
    binary = data[0][i] + data[0][i+1] + data[0][i+2]

    List.append(binary)


print(List)
print(len(List))



app = Flask(__name__)

@app.route('/') #dont forget @
def home():
    global List

    dict = {
         '000' :'red' ,
         '001' :'white' ,
         '010' :'yellow' ,
         '011' :'blue' ,
         '100' : 'black' ,
         '110' : 'green' 
    }
    


    
    arr = []

    
    for i in range(0,len(List), 9):
        row = []
        row.append(dict[List[i]])
        row.append(dict[List[i+1]])
        row.append(dict[List[i+2]])
        row.append(dict[List[i+3]])
        row.append(dict[List[i+4]])
        row.append(dict[List[i+5]])
        row.append(dict[List[i+6]])
        row.append(dict[List[i+7]])
        row.append(dict[List[i+8]])



        
        arr.append(row)

    return render_template('index.html', arr = arr)




if __name__ == '__main__':
    app.run(host ='127.0.0.1', port = 6969, debug = True)

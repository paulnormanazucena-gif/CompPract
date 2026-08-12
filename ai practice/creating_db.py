import json, pymongo


client = pymongo.MongoClient('127.0.0.1', 27017)
client.drop_database('CampusIT')
CampusIT = client.get_database('CampusIT')
Workstations = CampusIT.get_collection('Workstations')


#inserting json data

openfile = open('workstations.json', 'r')
data = json.load(openfile)
openfile.close()


Workstations.insert_many(data)


#documents = Workstations.find()

#for i in documents:
    #print(i)

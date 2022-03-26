#API COM FUNCONALIDADES BASICAS DE CRUD
#Rotas:
#   - / : homepage com explicações de uso

#   - /create/<nome>/<empresa>/<quantidade> : página de cadastro de informações a partir dos dados fornecidos

#   - /readall : página de leitura de todos os dados da base de dados

#   - /readone/<id>: página de leitura de um dado específico da base de dados. O parametro passado deve ser o ID da informação desejada.

#   - /update/<id>/<campo>/<mudança> : página de atualização de um dado na base de dados. O primeiro parametro selecionado o dado a ser mudado; o segundo parametro seleciona o campo a ser mudado; e o terceiro parametro define a nova informação para o campo.

#   - /delete : página para deletar um dado da base de dados. O parametro passado deve ser o ID a ser deletado.

from flask import Flask, jsonify,render_template
from csv import writer,reader
from datetime import datetime
import random
import string

app = Flask(__name__)

#_______________________________________________________
#HomePage
@app.route('/')
def homepage():
    
  return render_template("index.html")
#_______________________________________________________
#Create
@app.route('/create/<name>/<company>/<amount>')
def create(name,company,amount):
  id="".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
  created_at = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
  data_info = [id,name,company,created_at,amount]

  with open('data.csv','a') as file:
    csv_writer = writer(file)
    csv_writer.writerow(data_info)

    
  return "Created"  
#_______________________________________________________

  
#Read all 
@app.route('/readall')
def readall():
  with open('data.csv','r') as file:
    data_read = reader(file)
    data_dict = {}
    data_amount=0
    for row in data_read:
      if (data_amount>0):
        data_dict.update({"data"+str(data_amount): row})
      data_amount+=1
      
  return jsonify(data_dict)
 #_______________________________________________________

  
#Read a single data
@app.route('/readone/<id>')
def readone(id):
  with open('data.csv','r') as file:
    data_read = reader(file)
    data_dict = {}
    for row in data_read:
      if (id == row[0]):
       data_dict = {"data1":row}
    if(data_dict=={}):
       data_dict = {"data0":"not found"}
  return jsonify(data_dict)
#_______________________________________________________

  
#Update
@app.route('/update/<id>/<field>/<change>')
def update(id,field,change):
  
  updated_list = []
  is_changed = False
  response = 'Not found'
  
  with open('data.csv','r') as file:
    data_read = reader(file)
    for row in data_read:
      if (id == row[0]):
        if(field=='name'):
          row[1] = change
          is_changed = True
        elif(field=='company'):
          row[2] = change
          is_changed = True
        elif(field=='amount'):
          row[4] = change
          is_changed = True
      updated_list.append(row)

      
  if(is_changed):  
    with open('data.csv','w+') as file:
      csv_writer = writer(file)
      csv_writer.writerows(updated_list)
    response = 'Updated'
    
  return response
#_______________________________________________________

  
#Delete
@app.route('/delete/<id>')
def delete(id):
  is_deleted = False
  response = 'Not found'
  updated_list = []
  with open('data.csv','r') as file:
    data_read = reader(file)
    for row in data_read:
      if (id != row[0]):
       updated_list.append(row)
      else:
        response='Deleted'
        is_deleted = True
      
      
  if(is_deleted):  
    with open('data.csv','w+') as file:
      csv_writer = writer(file)
      csv_writer.writerows(updated_list)
  return response
#_______________________________________________________

#Run
app.run(host='0.0.0.0')
#_______________________________________________________


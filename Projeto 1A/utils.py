import json
from os import path
from database import *

def extract_route(requisicao):
    lista1 = requisicao.split(" /")
    lista2 = lista1[1].split(" ")

    return lista2[0]

def read_file(filepath):
    string = str(filepath)
    ext = string.split(".")
    type = ext[1]
    # print(type)
    if type == "txt" or type == "html" or type == "css" or type =="js":
        with open(filepath, "rt", encoding="UTF-8") as text:
            readText = text.read()
            return readText
    else:
        with open(filepath, "rb") as bin:
            readBin = bin.read()
            return readBin      

def load_data(fileJson):
    jsonPath = 'data/' + fileJson
    with open(jsonPath, 'rt', encoding="UTF-8") as jsonFile:
        readData = jsonFile.read()
        finalData = json.loads(readData)
        return finalData

def load_template(fileName):
    filepath = 'templates/' + fileName
    with open (filepath, 'r', encoding='UTF-8') as fileForm:
        read = fileForm.read()
    return read
    
def recebe_post_json(note):
    filename = 'data/notes.json'
    entry = note
    with open(filename, "rt", encoding="UTF-8") as file:
        # readText = file.read()
        data = json.load(file)
    data.append(entry)
    string = json.dumps(data, indent=4)
    with open(filename, "w", encoding="UTF-8") as file2:
        file2.write(string)

def adicionar(dict,db):
    db.add(Note(title= dict['titulo'], content=dict['detalhes']))

def delete(id,db):
    db.delete(id)

def update(dict,db):
    db.update(Note(id=dict['id'], title=dict['titulo'], content=dict['detalhes']))

def build_response(body='', code=200, reason='OK', headers=''):
    if len(headers) != 0:
        convertido = ("HTTP/1.1 " + str(code)+ " " + reason + '\n' + headers + '\n\n' + body).encode()  
    else:
         convertido = ("HTTP/1.1 " + str(code)+ " " + reason + '\n\n' + body).encode()  
    return convertido

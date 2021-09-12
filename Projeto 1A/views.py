from json import load
import json
from utils import adicionar, delete, load_data, load_template, build_response, adicionar, update
import urllib.parse
from database import *
from os import error, replace

db = Database('data/notes')

def index(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for keyValue in corpo.split('&'):
            key, value = keyValue.split('=')
            params[key] = urllib.parse.unquote_plus(value, encoding='utf-8', errors='replace')  

        if params['method'] == 'POST':
            adicionar(params, db)
        elif params['method'] == 'DELETE':
            db.delete(params['id'])
        elif params['method'] == 'UPDATE':
            db.update(Note(id=params["id"], title=params["title"], content=params["details"]))

        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados.id, title=dados.title, details=dados.content)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))



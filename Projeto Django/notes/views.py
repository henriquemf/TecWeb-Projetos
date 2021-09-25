from django.shortcuts import render, redirect
from .models import Note
from .models import Tags

#----------------- Notes --------------------

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        Note(title = title, content = content).save()
        return redirect('index')
    else:
        allNotes = Note.objects.all()
        return render(request, 'notes/notes.html', {'notes': allNotes})

def noteDelete(request):
    if request.method == 'POST':
        Note.objects.get(id=request.POST.get('id')).delete()
        return redirect('index')

def noteUpdate(request,id):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    # print("REQUEST AQUI {0}".format(request.POST))
    # print("TITLE AQUI {0}".format(title))
    # print(content)
    #o erro era que estava em português aqui e em inglês no html...
    Note.objects.filter(id=id).update(title = title, content = content)
    return redirect('index')

#----------------- Tags --------------------

def tagId(request):
    allTags = Tags.objects.all()
    return render(request, 'notes/viewTags.html', {'notes': allTags})

def tagContent(request, tagid):
    pass
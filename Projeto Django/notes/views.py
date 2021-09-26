from django.shortcuts import render, redirect
from .models import Note,Tags

#----------------- Notes --------------------

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag, checkCreation = Tags.objects.get_or_create(tag=request.POST.get('tag'))
        if checkCreation:
            tag.save()
        Note(title = title, content = content, tag = tag).save()
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
    #o erro era que estava em português aqui e em inglês no html... (ATENÇÃO A ISSO!)
    tag, checkCreation = Tags.objects.get_or_create(tag=request.POST.get('tag'))
    if checkCreation:
        tag.save()
    Note.objects.filter(id=id).update(title = title, content = content, tag=tag)
    return redirect('index')

#----------------- Tags --------------------

def tagId(request):
    return render(request, 'notes/viewTags.html', {'notes': Tags.objects.all()})

def tagContent(request, tagid):
    return render(request, 'notes/viewTaggedNotes.html', {'notes': Note.objects.filter(tag=tagid)})
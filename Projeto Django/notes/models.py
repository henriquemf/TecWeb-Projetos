from django.db import models

class Tags(models.Model):
    tag = models.CharField(max_length=200,null=True, blank=True)

    #Agora é possível ler o nome das Tags na página do Admin
    def __str__(self):
        return  str(self.id)+". "+str(self.tag)

class Note(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    content = models.TextField(blank=True,null=True)
    tag = models.ForeignKey(Tags, blank=True, null = True, on_delete=models.SET_NULL) 
    #Um para Muitos, ler mais em: https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/
    
    def __str__(self):
        return  str(self.id)+". "+str(self.title)
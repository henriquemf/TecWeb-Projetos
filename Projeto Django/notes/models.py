from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    content = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return  str(self.id)+". "+str(self.title)

class Tags(models.Model):
    tags = models.CharField(max_length=200,null=True, blank=True)
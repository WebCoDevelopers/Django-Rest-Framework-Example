from django.db import models
from django.utils.encoding import smart_text;
class Paradigm(models.Model):
    paradigm=models.CharField(max_length=256);
    def __str__(self):
        return smart_text(self.paradigm);
class Language(models.Model):
    name=models.CharField(max_length=256);
    paradigm=models.ForeignKey(Paradigm,on_delete=models.CASCADE);
    def __str__(self):
        return smart_text(self.name);
class Programmer(models.Model):
    name=models.CharField(max_length=256);
    languages=models.ManyToManyField(Language);
    def __str__(self):
        return smart_text(self.name);

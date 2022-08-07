from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Pergunta')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='Data')
    show = models.BooleanField(default=True, verbose_name='Mostrar')    
    
    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='Opção')
    votes = models.IntegerField(default=0, verbose_name='Votos')
    
    def __str__(self):
        return self.choice_text
    



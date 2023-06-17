from django.db import models


# Create your models here.
class Customer(models.Model):
    '''Клиенты'''
    nickname = models.CharField('Никнейм', max_length=100, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=15, unique=True)
    blocked = models.BooleanField('Заблокирован', default=False)
    date_reg = models.DateTimeField('Дата регистрации', auto_now_add=True)

    class Meta:
      verbose_name = 'Клиент'
      verbose_name_plural = 'Клиенты'
      
    def __str__(self):
        return f'{self.nickname} | {self.phone}'


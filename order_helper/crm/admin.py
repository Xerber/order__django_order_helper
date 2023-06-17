from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''Клиенты'''
    list_display = ("nickname","phone","blocked", "date_reg")
    list_editable = ("blocked",)
    readonly_fields = ("date_reg",)
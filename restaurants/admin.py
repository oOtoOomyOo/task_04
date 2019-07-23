from django.contrib import admin
from .models import Restaurant
# Register your models here.

admin.site.register(Restaurant)

def __str__(self):
	return self.name
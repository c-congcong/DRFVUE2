from django.contrib import admin

# Register your models here.
from user import models

admin.site.register(models.Employee)
admin.site.register(models.User)

from django.contrib import admin
from .models import *


# Register your models here.

admin.site.site_header = 'SELF ASSESSMENT SYSTEM '
admin.site.register(Users)
admin.site.register(Plan)
admin.site.register(Income)
admin.site.register(Expenses)

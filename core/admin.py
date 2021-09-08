from django.contrib import admin
from .models import *
# Register your models here.
class IndexAdmin(admin.ModelAdmin):
    exclude = ('count',)
admin.site.register(Index,IndexAdmin)

admin.site.register(Comment)

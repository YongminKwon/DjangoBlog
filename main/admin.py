from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields' : ['postname']}), 
        ('Contents', {'fields' : ['contents']}),
        ('Photo', {'fields' : ['mainphoto'], 'classes': ['collapse']}),
    ]

admin.site.register(Post, PostAdmin)


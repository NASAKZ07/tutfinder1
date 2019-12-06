from django.contrib import admin
from .models import ToDoList, Item, Post
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Post)
  
# Register your models here.

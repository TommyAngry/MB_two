from django.contrib import admin
from .models import  Post
from .models import  Post, Comments

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    ''' лист дисплей чтобы данные по заголовку и автору красиво отображались'''

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("name", "post")
    ''' лист дисплей чтобы данные по заголовку и автору красиво отображались'''

# Register your models here.

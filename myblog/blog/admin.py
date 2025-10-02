from django.contrib import admin
from .models import  Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    ''' лист дисплей чтобы данные по заголовку и автору красиво отображались'''

# Register your models here.

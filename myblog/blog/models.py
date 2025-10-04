from django.db import models

class Post(models.Model):
    '''данные о посте'''
    title = models.CharField('Заголовок записи', max_length=100)
    desciptions=models.TextField('Текст записи')
    author=models.CharField("Имя автора", max_length=100)
    date = models.DateField("Дата публикации")
    img = models.ImageField("Изображения", upload_to="image/%Y")

    def __str__(self):
        return f"{self.title},{self.author}"

    class Meta:
        verbose_name="Запись"  "для удобо читаемого единственного имени модели"
        verbose_name_plural="Записи"




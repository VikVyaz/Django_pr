from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='photos/blog_img/', verbose_name='Превью', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True)
    view_counter = models.PositiveIntegerField(verbose_name='Счетчик просмотров', default=0)

    def __str__(self):
        return f'Блоговая запись "{self.title}"'

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'
        ordering = ['id']
        db_table = 'blog_entry'

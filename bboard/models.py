from django.db import models
# Create your models here.


class Bb(models.Model):
    BUY = 'b'
    SELL = 's'
    CHANGE = 'c'
    KINDS = (
        (BUY, 'Куплю'), (SELL, 'Продам'), (CHANGE, 'Обменяю'),
    )
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    kind = models.CharField(max_length=1, choices=KINDS, default='s', verbose_name='Тип')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

    # def title_and_price(self): 
    #     if self.price:
    #         return '%s (%.2f)' % (self.title, self.price) 
    #     else:
    #         return self.title

class Rubric(models.Model):
    name = models.CharField(max_length=15, db_index=True, verbose_name='Название')
    order = models.SmallIntegerField(default=1, db_index=True)

    def __str__(self):
        return self.name
    
    # def get_absolute_url():
    #     return "/bboard/%s/" % self.pk

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['order' ,'name']
from django.db import models
from django.utils import timezone


class Subscribe(models.Model):
    chat_id = models.IntegerField(verbose_name='ID Telegram чата для рассылки')

    time = models.TimeField(
        verbose_name='Время рассылки', default=timezone.now()
    )

    last_date_check = models.DateField(
        verbose_name='Последняя дата рассылки в чат', default=timezone.now().date()
    )

    def __str__(self):
        return f'Подписка {self.chat_id} | {self.time}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

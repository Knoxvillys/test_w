from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Mailing(models.Model):
    start_data = models.DateTimeField(
        verbose_name="Начало рассылки"
    )
    finish_data = models.DateTimeField(
        verbose_name="Окончание рассылки"
    )
    start_time = models.TimeField(
        verbose_name="Время начала рассылки"
    )
    finish_time = models.TimeField(
        verbose_name="Время начала рассылки"
    )
    text = models.TimeField(
        verbose_name="Текст сообщения",
        max_length=150
    )
    tag = models.CharField(
        verbose_name="Фильтр по тегу",
        max_length=100, blank=True
    )
    operator_code = models.CharField(
        verbose_name="Фильтр по коду оператора",
        max_length=100,
        blank=True
    )

    @property
    def to_send(self):
        now = timezone.now()
        if self.start_data <= now <= self.finish_data:
            return True
        else:
            return False

    def __str__(self):
        return f"Рассылка {self.id} от {self.start_data}"

    class Meta:
        verbose_name = "Рассылки"
        verbose_name_plural = "Рассылки"
    
    
class Client(models.Model):
    phone_valid = RegexValidator(
        regex="^7\w{10}$",
        message="Номер клиента должен быть в формате 7XXXXXXXXXX (X - цифра от 0 до 9)",
    )
    phone = models.PositiveIntegerField(
        verbose_name="Номер мобильного телефона",
        validators=[phone_valid]
    )
    code = models.PositiveIntegerField(
        verbose_name="Код оператора"
    )
    tag = models.CharField(
        verbose_name="Фильтр по тегу",
        max_length=100,
        blank=True
    )
    time_zone = models.CharField(
        verbose_name="Часовой пояс",
        max_length=10
         )
    
    def __str__(self):
        return f"Клиент {self.id} с номером {self.phone}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Message(models.Model):
    SENT = "sent"
    PROCEEDED = "proceeded"
    FAILED = "failed"

    STATUS = [
        (SENT, "Sent"),
        (PROCEEDED, "Proceeded"),
        (FAILED, "Failed"),
    ]
    data = models.DateTimeField(
        verbose_name="Дата сообщения",
        auto_now_add=True
    )
    status = models.CharField(
        verbose_name="Статус отправки",
        max_length=20,
        choices=STATUS
    )
    mailing = models.ForeignKey(
        "Mailing",
        verbose_name="messages",
        on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        "Client",
        verbose_name="messages",
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"Сообщение {self.id} с текстом {self.mailing} для {self.client}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
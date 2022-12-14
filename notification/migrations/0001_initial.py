# Generated by Django 3.2.16 on 2022-11-17 10:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(message='Номер клиента должен быть в формате 7XXXXXXXXXX (X - цифра от 0 до 9)', regex='^7\\w{10}$')], verbose_name='Номер мобильного телефона')),
                ('code', models.PositiveIntegerField(verbose_name='Код оператора')),
                ('tag', models.CharField(blank=True, max_length=100, verbose_name='Фильтр по тегу')),
                ('time_zone', models.CharField(max_length=10, verbose_name='Часовой пояс')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_data', models.DateTimeField(verbose_name='Начало рассылки')),
                ('finish_data', models.DateTimeField(verbose_name='Окончание рассылки')),
                ('start_time', models.TimeField(verbose_name='Время начала рассылки')),
                ('finish_time', models.TimeField(verbose_name='Время начала рассылки')),
                ('text', models.TimeField(max_length=150, verbose_name='Текст сообщения')),
                ('tag', models.CharField(blank=True, max_length=100, verbose_name='Фильтр по тегу')),
                ('operator_code', models.CharField(blank=True, max_length=100, verbose_name='Фильтр по коду оператора')),
            ],
            options={
                'verbose_name': 'Рассылки',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Дата сообщения')),
                ('status', models.CharField(choices=[('sent', 'Sent'), ('proceeded', 'Proceeded'), ('failed', 'Failed')], max_length=20, verbose_name='Статус отправки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.client', verbose_name='messages')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.mailing', verbose_name='messages')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]

from rest_framework import serializers

from .models import Client, Mailing, Message


class ClientSerializer(serializers.ModelSerializer):
    """
    Сериализатор Клиента
    """
    class Meta:
        model = Client
        fields = ('phone', 'code', 'tag', 'time_zone', 'id',)


class MessageSerializer(serializers.ModelSerializer):
    """
    Сериализатор сообщений
    """
    class Meta:
        model = Message
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    """
    Сериализатор рассылки
    """
    class Meta:
        model = Mailing
        fields = '__all__'

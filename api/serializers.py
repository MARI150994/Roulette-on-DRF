from rest_framework import serializers

from .models import Round, Log


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('user_id', 'cell', 'round_id')
        read_only_fields = ('cell', 'round_id')


class RoundSerializer(serializers.ModelSerializer):
    users_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Round
        fields = ('id', 'users_count')
        read_only_fields = ('id',)

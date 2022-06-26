from django.db import models
from django.core.validators import MinValueValidator


class Round(models.Model):
    current_attempt = models.PositiveSmallIntegerField('current attempt number')

    def __str__(self):
        return f'Round: {self.id}, attempt: {self.current_attempt}'


class Log(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='logs')
    user_id = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    cell = models.PositiveSmallIntegerField('number of cell')

    def __str__(self):
        return f'Log for user id: {self.user_id}, round: {self.round_id}'

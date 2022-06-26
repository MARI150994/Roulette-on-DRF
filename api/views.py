from typing import List

from django.db.models import F, Count
from django.db import connection
from rest_framework import generics
from rest_framework.response import Response

from .serializers import LogSerializer, RoundSerializer
from .utils import select_cell
from .models import Round, Log


class Roulette(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    # for POST method
    def perform_create(self, serializer):
        # if no Round yet, create new Round and use it
        if Round.objects.all().exists():
            current_round = Round.objects.last()
        else:
            current_round = Round.objects.create(current_attempt=1)
        # if not last attempt in round - return cell number, increase current attempt number
        if current_round.current_attempt <= 10:
            used_cells: List = list(current_round.logs.values_list('cell', flat=True))
            cell: int = select_cell(used_cells)
            current_round.current_attempt = F('current_attempt') + 1
            current_round.save()
        # if last attempt in round - return cell = 11 (jackpot) and create new round
        else:
            cell = 11
            Round.objects.create(current_attempt=1)
        # create Log instance with current round number and with cell number
        serializer.save(round=current_round, cell=cell)

    # for GET method
    def list(self, request, *args, **kwargs):
        # info about each round
        queryset = self.filter_queryset(
            Round.objects.annotate(users_count=Count('logs__user_id', distinct=True))
        )
        serializer = RoundSerializer(queryset, many=True)
        # info about top 5 users
        top_users = Log.objects.values('user_id').annotate(count=Count('user_id')).order_by('-count')[:5]
        top_users_grouped = Log.objects.values('user_id', 'round_id').\
            annotate(c=Count('user_id')).\
            filter(user_id__in=top_users.values('user_id'))
        with connection.cursor() as cursor:
            query = f'SELECT x.user_id, sum(x.c), round(Avg(x.c), 1) as avg ' \
                    f'FROM ({top_users_grouped.query}) as x ' \
                    f'group by x.user_id ' \
                    f'order by sum(x.c) desc'
            cursor.execute(query)
            statistics = []
            top_users_statistics = cursor.fetchall()
            for user, total, avg in top_users_statistics:
                statistics.append(
                    {'user_id': user, 'total': total, 'average': avg}
                )
        return Response({'top_users': statistics, 'round_info': serializer.data}, status=200)

## 효정: 누적 달성도 그래프
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, datetime, timedelta
from schedules.models import Schedule
from .models import Achievement
from .serializers import StatusSerializer


class TotalGraphViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Schedule.objects.filter(writer=self.request.user)
        before = date.today() - timedelta(days=15)
        after = date.today() + timedelta(days=15)
        # today = date.today() - timedelta(days=15)
        # print(today)

        # print(self.request.query_params)
        # start_date__range = [date1, date2]
        # queryset = queryset.filter(start_date=datetime.strptime(str(today),'%Y-%m-%d'))
        queryset = queryset.filter(start_date=datetime.strptime(str(before), '%Y-%m-%d'))

        for i in range(0, 31):
            before = before + timedelta(days=i)
            queryset = queryset.filter(start_date=datetime.strptime(str(before), '%Y-%m-%d'))
            finished_count = 0
            total_schedules_day = queryset.count()
            for query in queryset:
                if query.is_finished == True:
                    finished_count += 1
                # print(query)
                # print(query.is_finished)

            total_percent = total_schedules_day
            achievement = Achievement.objects.create(
                date=before,
                finished_schedules_day=finished_count,
                total_schedules_day=total_schedules_day,
                total_percent=total_percent
            )

            achievement.save()
        before = datetime.strptime(str(before), '%Y-%m-%d')
        after = datetime.strptime(str(after), '%Y-%m-%d')
        queryset = Achievement.objects.filter(start_date__range=[before, after])

        # s = queryset.count()
        # print(s)
        # print(f'count: {finished_count}')

        # # 하루 일일 달성도
        # total_percent = models.FloatField(default=0)
        # # 하루 전체 일정 수
        # total_schedules_day = models.IntegerField(default=0)
        # # 하루 달성 일정 수
        # finished_schedules_day = models.IntegerField(default=0)

        # 하루 일일 달성도

        # print(queryset[0].is_finished)

        # elif 'month' in self.request.query_params:
        #     date1 = datetime.strptime(self.request.query_params['month'], '%Y-%m')
        #     date2 = datetime(date1.year, date1.month + 1, date1.day)
        #     queryset = queryset.filter(start_date__range=[date1, date2])
        return queryset

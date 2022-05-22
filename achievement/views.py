from datetime import date, datetime, timedelta

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from schedules.models import Schedule

from .models import Achievement
from .serializers import AchievementSerializer


class TotalGraphViewSet(viewsets.ModelViewSet):
    # ViewSet 설정
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = (IsAuthenticated,)

    # 무조건 GET 방식으로 해야 함
    def get_queryset(self, queryset=None):
        # queryset = Schedule.objects.all()
        # 오늘 날짜를 기준으로 -15일 ~ +15일 기간을 구할 것임
        today = date.today() - timedelta(days=15)

        # 한달(30번) 돌리면서 Achievement에 저장
        for _ in range(0, 31):

            # 변수 선언, 초기화
            total_schedules_day = 0  # 전체 일정 개수
            finished_schedules_day = 0  # 완료 일정 개수
            total_percent = 0  # 일일 달성도

            # 하루가 지날 때마다 today에 +1
            today += timedelta(days=1)

            # Schedule에서 before에 해당하는 일정들 전부 가져오기
            schedule_list = Schedule.objects.filter(writer=self.request.user,
                                                    start_date=datetime.strptime(str(today), '%Y-%m-%d'))

            # 날짜에 해당 되는 일정이 있다면 아래 실행
            if schedule_list:
                total_schedules_day = schedule_list.count()  # 전체 일정 개수

                # 같은 날짜의 일정을 하나씩 확인한다.
                for schedule in schedule_list:
                    # 일정이 완료된 상태라면 완료 일정 개수 += 1
                    if schedule.is_finished:
                        finished_schedules_day += 1

                # 일일 달성도 = 완료 일정 개수 / 전체 일정 개수
                total_percent = finished_schedules_day / total_schedules_day

            achievement = Achievement.objects.filter(writer=self.request.user, date=today).update_or_create(
                finished_schedules_day=finished_schedules_day,
                total_schedules_day=total_schedules_day,
                total_percent=total_percent, # 일일 달성도
                date=today,
                writer=self.request.user
            )

            # 테스트용 코드 (1)
            # print(f'{i}: {today} / daily_percent: {achievement} / daily_percent: {daily_percent}')
            # achievement.save()

        # 오늘 날짜로부터터 -15일 ~ +15 범위를 필터링
        before = date.today() - timedelta(days=15) # -15일
        after = date.today() + timedelta(days=15) # +15일

        before = datetime.strptime(str(before), '%Y-%m-%d')
        after = datetime.strptime(str(after), '%Y-%m-%d')
        achievement_list = Achievement.objects.filter(date__range=[before, after])

        # 테스트용 코드 (2)
        # print(f'achievement_list: {achievement_list}')

        return achievement_list

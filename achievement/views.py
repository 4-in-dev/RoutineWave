from datetime import date, datetime, timedelta

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from schedules.models import Schedule
from .models import Achievement, Status, Rank
from .serializers import AchievementSerializer, StatusSerializer, RankSerializer


## 일일 달성도 그래프
class AchievementViewSet(viewsets.ModelViewSet):
    # ViewSet 설정
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = (IsAuthenticated,)

    # 무조건 GET 방식으로 해야 함
    def get_queryset(self, queryset=None):
        # 오늘 날짜를 기준으로 -30일 기간을 구할 것임
        today = date.today() - timedelta(days=30)

        # 한달(30번) 돌리면서 Achievement에 저장
        for _ in range(0, 31):

            # 변수 선언, 초기화
            total_schedules_day = 0  # 전체 일정 개수
            finished_schedules_day = 0  # 완료 일정 개수
            total_percent = 0  # 일일 달성도

            # 하루가 지날 때마다 today에 +1
            today += timedelta(days=1)

            # Schedule에서 today에 해당하는 일정들 전부 가져오기
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
                total_percent=total_percent,  # 일일 달성도
                date=today,
                writer=self.request.user
            )

            # 테스트용 코드 (1)
            # print(f'{i}: {today} / daily_percent: {achievement} / daily_percent: {daily_percent}')
            # achievement.save()

        # 오늘 날짜로부터 -30일 범위를 필터링
        before = date.today() - timedelta(days=30)  # -30일
        after = date.today() + timedelta(days=1)# 오늘

        before = datetime.strptime(str(before), '%Y-%m-%d')
        after = datetime.strptime(str(after), '%Y-%m-%d')
        achievement_list = Achievement.objects.filter(date__range=[before, after])

        # 테스트용 코드 (2)
        # print(f'achievement_list: {achievement_list}')

        return achievement_list



## 스텟별 달성도 그래프
class StatusViewSet(viewsets.ModelViewSet):
    # ViewSet 설정
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAuthenticated,)

    # 무조건 GET 방식으로 해야 함
    def get_queryset(self, queryset=None):

        # 변수 선언, 초기화
        hp = 0  # 체력
        int = 0  # 지력
        will = 0  # 근성, 의지
        exp = 0  # 경험
        money = 0  # 재력
        ten = 0  # 행복

        # 오늘 날짜로부터 -30일 범위를 필터링
        before = date.today() - timedelta(days=30)  # -30일
        after = date.today() + timedelta(days=1)  # 오늘

        before = datetime.strptime(str(before), '%Y-%m-%d')
        after = datetime.strptime(str(after), '%Y-%m-%d')

        ## 체력 달성도
        total_hp = Schedule.objects.filter(writer=self.request.user, status='hp')
        if total_hp:
            finished_hp = Schedule.objects.filter(writer=self.request.user, status='hp', is_finished=1)
            total_hp_cnt = total_hp.count()
            finished_hp_cnt = finished_hp.count()
            hp = finished_hp_cnt / total_hp_cnt

        ## 지력 달성도
        total_int = Schedule.objects.filter(writer=self.request.user, status='int')
        if total_int:
            finished_int = Schedule.objects.filter(date__range=[before, after], writer=self.request.user, status='int',
                                                   is_finished=1)
            total_int_cnt = total_int.count()
            finished_int_cnt = finished_int.count()
            int = finished_int_cnt / total_int_cnt

        ## 근성 달성도
        total_will = Schedule.objects.filter(writer=self.request.user, status='will')
        if total_will:
            finished_will = Schedule.objects.filter(writer=self.request.user, status='will', is_finished=1)
            total_will_cnt = total_will.count()
            finished_will_cnt = finished_will.count()
            will = finished_will_cnt / total_will_cnt

        ## 경험 달성도
        total_exp = Schedule.objects.filter(writer=self.request.user, status='exp')
        if total_exp:
            finished_exp = Schedule.objects.filter(writer=self.request.user, status='exp', is_finished=1)
            total_exp_cnt = total_exp.count()
            finished_exp_cnt = finished_exp.count()
            exp = finished_exp_cnt / total_exp_cnt

        ## 재력 달성도
        total_money = Schedule.objects.filter(writer=self.request.user, status='money')
        if total_money:
            finished_money = Schedule.objects.filter(writer=self.request.user, status='money', is_finished=1)
            total_money_cnt = total_money.count()
            finished_money_cnt = finished_money.count()
            money = finished_money_cnt / total_money_cnt

        ## 행복 달성도
        total_ten = Schedule.objects.filter(writer=self.request.user, status='ten')
        if total_ten:
            finished_ten = Schedule.objects.filter(writer=self.request.user, status='ten', is_finished=1)
            total_ten_cnt = total_ten.count()
            finished_ten_cnt = finished_ten.count()
            ten = finished_ten_cnt / total_ten_cnt

        status = Status.objects.filter(writer=self.request.user).update_or_create(
            writer=self.request.user, hp=hp, int=int, will=will, exp=exp, money=money, ten=ten)

        return status



## 사용자별 랭크
class RankViewSet(viewsets.ModelViewSet):

    # ViewSet 설정
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # 오늘 날짜로부터 -30일 범위를 필터링
        before = date.today() - timedelta(days=30)  # -30일
        after = date.today() + timedelta(days=1)  # 오늘

        before = datetime.strptime(str(before), '%Y-%m-%d')
        after = datetime.strptime(str(after), '%Y-%m-%d')

        finished_list = Schedule.objects.filter(writer=self.request.user, start_date__range=[before, after], is_finished=1)
        finished_cnt = finished_list.count()

        if finished_cnt < 1:
            user_rank = 'D'
        elif finished_cnt < 2:
            user_rank = 'C'
        elif finished_cnt < 3:
            user_rank = 'B'
        elif finished_cnt < 4:
            user_rank = 'A'
        elif finished_cnt < 5:
            user_rank = 'S'

        rank = Rank.objects.filter(writer=self.request.user).update_or_create(writer=self.request.user, rank=user_rank)

        return rank

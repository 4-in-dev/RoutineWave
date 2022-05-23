import datetime as dt
from datetime import datetime, time, timedelta

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User

from .models import Event
from .serializers import EventSerializer, UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(user=self.request.user,
                        end_date=self.request.data['end_date']
                            if 'end_date' in self.request.data else self.request.data['start_date'],
                        end_time=self.request.data['end_time'] if 'end_time' in self.request.data else time(23, 59)
                        )

    def get_queryset(self):
        queryset = Event.objects.filter(user=self.request.user)
        print(self.request.query_params)
        if 'day' in self.request.query_params:
            print(self.request.query_params)
            queryset = queryset.filter(start_date=datetime.strptime(self.request.query_params['day'], '%Y-%m-%d'))
        elif 'month' in self.request.query_params:
            date1 = datetime.strptime(self.request.query_params['month'], '%Y-%m')
            date2 = datetime(date1.year, date1.month + 1, date1.day)
            queryset = queryset.filter(start_date__range=[date1, date2])
        return queryset

    # def get_queryset(self):
    #     """
    #     This function returns the appropriate events depending on the
    #     args given in the get request
    #     """
    #     queryset = self.queryset
    #
    #     day = self.request.query_params.get('day')
    #     month = self.request.query_params.get('month')
    #     year = self.request.query_params.get('year')
    #     query = self.request.query_params.get('query')
    #
    #     if (not query) or (not year):
    #
    #         # Here we get users who have shared their calendar with
    #         # the current user.
    #         users = [self.request.user]
    #         users += list(self.request.u)
    #         print(users)
    #         queryset = self.queryset.filter(author__in=users)
    #
    #         if query:
    #             return queryset.filter(title__contains=query)
    #
    #         if day and month and year:
    #             day, month, year = [int(x) for x in [day, month, year]]
    #             return queryset.filter(event_date__contains=dt.date(year, month, day))
    #
    #         if month and year:
    #             return queryset.filter(event_date__month=month,
    #                                    event_date__year=year)
    #

    #     return queryset

    # @login_required
    # def currenttodos(request):
    #     todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    #     return render(request, 'todo/currenttodos.html', {'todos': todos})
    #
    # @login_required
    # def completedtodos(request):
    #     todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    #     return render(request, 'todo/completedtodos.html', {'todos': todos})

import datetime

movies = [
    {
        'info': ('Avengers', 2018, {'Thor': 'Chris Hemsworth'}),
    },
]


user = None
today = datetime.datetime.today()


class Check:
    pass


class UserAction:
    pass


class Sum:
    pass


async def foo():
    if (
        (user and user.is_authorized)
        and user.subscriptions.filter(start_date__lt=today, end_date__gt=today).exists()
        and (
            user.total_credits_added
            - Check.objects.filter(user=user).aggregate(Sum('price'))['check__sum']
        )
        and (
            UserAction.objects.filter(user=user).last().datetime
            > today - datetime.timedelta(days=10)
        )
    ):
        await bar()
        pass


async def bar():
    return 'bar'


weird_container = []
sublist = weird_container[10:datetime.datetime.today(), None]

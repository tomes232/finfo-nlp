import datetime
from datetime import date

## Grabs the datetime object at 6:00 PM the previous day. If Saturday or Sunday grabs Thursday @ 6:00PM
def date_func(day=7):
    today = date.today()
    date_ = today - datetime.timedelta(days=day)
    date_ = datetime.datetime(date_.year,date_.month,date_.day,18,0,0)
    print(today.weekday())
    if today.weekday()==5:
        days = datetime.timedelta(1)
        date_ = date_ - days
    elif today.weekday()==6:
        days = datetime.timedelta(2)
        date_ = date_ - days
    return date_
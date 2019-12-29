from rest_framework import generics
import datetime

from quotes.models import Quote
from quotes.models import QuoteCategory

from .serializers import QuoteSerializer
from .serializers import QuoteCategorySerializer

class QuoteAPIView(generics.ListAPIView):
    quote = Quote.objects.all()
    for s in quote:
        id = s.id
        create_time = s.created
        update_time = s.modified
        current_time = datetime.datetime.now()

        create_times = str(create_time)
        create_timing = create_times[0:19]

        update_times = str(update_time)
        update_timing = update_times[0:19]

        current_times = str(current_time)
        current_timing = current_times[0:19]

        date_time_obj = datetime.datetime.strptime(str(create_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj1 = datetime.datetime.strptime(str(update_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj2 = datetime.datetime.strptime(str(current_timing), '%Y-%m-%d %H:%M:%S')

        create_date = date_time_obj.date()
        update_date = date_time_obj1.date()
        current_date = date_time_obj2.date()

        create_clock = date_time_obj.time()
        update_clock = date_time_obj1.time()
        current_clock = date_time_obj2.time()

        update_clock = str(update_clock)
        current_clock = str(current_clock)



        print(create_date)
        print(update_date)
        print(current_date)

        print(create_clock)
        print(update_clock)
        print(current_clock)

        if update_date == current_date :
            utime = update_clock.split(":")
            hour = utime[0]
            minute = utime[1]

            total = int(hour)*60 + int(minute)

            print(hour)
            print(minute)

            ctime = current_clock.split(":")
            hours = ctime[0]
            minutes = ctime[1]

            print(hours)
            print(minutes)

            totals = int(hours)*60 + int(minutes)

            calculation = int(totals)-int(total)

            if calculation>5:
                Quote.objects.filter(pk=id).delete()

            print(calculation)

    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteAPIDetailView(generics.RetrieveUpdateAPIView):
    quote = Quote.objects.all()
    for s in quote:
        id = s.id
        create_time = s.created
        update_time = s.modified
        current_time = datetime.datetime.now()

        create_times = str(create_time)
        create_timing = create_times[0:19]

        update_times = str(update_time)
        update_timing = update_times[0:19]

        current_times = str(current_time)
        current_timing = current_times[0:19]

        date_time_obj = datetime.datetime.strptime(str(create_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj1 = datetime.datetime.strptime(str(update_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj2 = datetime.datetime.strptime(str(current_timing), '%Y-%m-%d %H:%M:%S')

        create_date = date_time_obj.date()
        update_date = date_time_obj1.date()
        current_date = date_time_obj2.date()

        create_clock = date_time_obj.time()
        update_clock = date_time_obj1.time()
        current_clock = date_time_obj2.time()

        update_clock = str(update_clock)
        current_clock = str(current_clock)

        print(create_date)
        print(update_date)
        print(current_date)

        print(create_clock)
        print(update_clock)
        print(current_clock)

        if update_date == current_date:
            utime = update_clock.split(":")
            hour = utime[0]
            minute = utime[1]

            total = int(hour) * 60 + int(minute)

            print(hour)
            print(minute)

            ctime = current_clock.split(":")
            hours = ctime[0]
            minutes = ctime[1]

            print(hours)
            print(minutes)

            totals = int(hours) * 60 + int(minutes)

            calculation = int(totals) - int(total)

            if calculation > 5:
                Quote.objects.filter(pk=id).delete()

            print(calculation)
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteAPINewView(generics.ListCreateAPIView):
    quote = Quote.objects.all()
    for s in quote:
        id = s.id
        create_time = s.created
        update_time = s.modified
        current_time = datetime.datetime.now()

        create_times = str(create_time)
        create_timing = create_times[0:19]

        update_times = str(update_time)
        update_timing = update_times[0:19]

        current_times = str(current_time)
        current_timing = current_times[0:19]

        date_time_obj = datetime.datetime.strptime(str(create_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj1 = datetime.datetime.strptime(str(update_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj2 = datetime.datetime.strptime(str(current_timing), '%Y-%m-%d %H:%M:%S')

        create_date = date_time_obj.date()
        update_date = date_time_obj1.date()
        current_date = date_time_obj2.date()

        create_clock = date_time_obj.time()
        update_clock = date_time_obj1.time()
        current_clock = date_time_obj2.time()

        update_clock = str(update_clock)
        current_clock = str(current_clock)

        print(create_date)
        print(update_date)
        print(current_date)

        print(create_clock)
        print(update_clock)
        print(current_clock)

        if update_date == current_date:
            utime = update_clock.split(":")
            hour = utime[0]
            minute = utime[1]

            total = int(hour) * 60 + int(minute)

            print(hour)
            print(minute)

            ctime = current_clock.split(":")
            hours = ctime[0]
            minutes = ctime[1]

            print(hours)
            print(minutes)

            totals = int(hours) * 60 + int(minutes)

            calculation = int(totals) - int(total)

            if calculation > 5:
                Quote.objects.filter(pk=id).delete()

            print(calculation)
    queryset = Quote.objects.all().order_by('-id')[:1] # latest quote
    serializer_class = QuoteSerializer

class QuoteCategoryAPIView(generics.ListAPIView):
    quote = Quote.objects.all()
    for s in quote:
        id = s.id
        create_time = s.created
        update_time = s.modified
        current_time = datetime.datetime.now()

        create_times = str(create_time)
        create_timing = create_times[0:19]

        update_times = str(update_time)
        update_timing = update_times[0:19]

        current_times = str(current_time)
        current_timing = current_times[0:19]

        date_time_obj = datetime.datetime.strptime(str(create_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj1 = datetime.datetime.strptime(str(update_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj2 = datetime.datetime.strptime(str(current_timing), '%Y-%m-%d %H:%M:%S')

        create_date = date_time_obj.date()
        update_date = date_time_obj1.date()
        current_date = date_time_obj2.date()

        create_clock = date_time_obj.time()
        update_clock = date_time_obj1.time()
        current_clock = date_time_obj2.time()

        update_clock = str(update_clock)
        current_clock = str(current_clock)

        print(create_date)
        print(update_date)
        print(current_date)

        print(create_clock)
        print(update_clock)
        print(current_clock)

        if update_date == current_date:
            utime = update_clock.split(":")
            hour = utime[0]
            minute = utime[1]

            total = int(hour) * 60 + int(minute)

            print(hour)
            print(minute)

            ctime = current_clock.split(":")
            hours = ctime[0]
            minutes = ctime[1]

            print(hours)
            print(minutes)

            totals = int(hours) * 60 + int(minutes)

            calculation = int(totals) - int(total)

            if calculation > 5:
                Quote.objects.filter(pk=id).delete()

            print(calculation)
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer

class QuoteAPISpecificView(generics.RetrieveAPIView):
    quote = Quote.objects.all()
    for s in quote:
        id = s.id
        create_time = s.created
        update_time = s.modified
        current_time = datetime.datetime.now()

        create_times = str(create_time)
        create_timing = create_times[0:19]

        update_times = str(update_time)
        update_timing = update_times[0:19]

        current_times = str(current_time)
        current_timing = current_times[0:19]

        date_time_obj = datetime.datetime.strptime(str(create_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj1 = datetime.datetime.strptime(str(update_timing), '%Y-%m-%d %H:%M:%S')
        date_time_obj2 = datetime.datetime.strptime(str(current_timing), '%Y-%m-%d %H:%M:%S')

        create_date = date_time_obj.date()
        update_date = date_time_obj1.date()
        current_date = date_time_obj2.date()

        create_clock = date_time_obj.time()
        update_clock = date_time_obj1.time()
        current_clock = date_time_obj2.time()

        update_clock = str(update_clock)
        current_clock = str(current_clock)

        print(create_date)
        print(update_date)
        print(current_date)

        print(create_clock)
        print(update_clock)
        print(current_clock)

        if update_date == current_date:
            utime = update_clock.split(":")
            hour = utime[0]
            minute = utime[1]

            total = int(hour) * 60 + int(minute)

            print(hour)
            print(minute)

            ctime = current_clock.split(":")
            hours = ctime[0]
            minutes = ctime[1]

            print(hours)
            print(minutes)

            totals = int(hours) * 60 + int(minutes)

            calculation = int(totals) - int(total)

            if calculation > 5:
                Quote.objects.filter(pk=id).delete()

            print(calculation)
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
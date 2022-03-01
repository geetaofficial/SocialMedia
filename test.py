from xmlrpc.client import boolean
import django
import os
from faker import Faker
import random
import warnings
from django.utils import timezone
from dateutil import relativedelta
from datetime import datetime, timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialMedia.settings')
django.setup()


def learn_query():
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/
    # q = Post.objects.all()
    # print(q.query)
    # print(q[:5])
    print("============================")
    # q1 = Post.objects.filter(title = "Ten at child office significant fact middle store be nature adult feel because base bar themselves car sing change.")
    # q1 = Post.objects.filter(title__icontains='Trip')
    # print(q1)
    # print(q1.query)

    # q2 = Post.objects.filter(id__in=[5,6,7])
    # print(q2)
    # print(q2.query)
    
    # q3 = Post.objects.filter(id__gt=5)
    # print(q3)
    # print(q3.query)
    
    # q4 = Post.objects.filter(id__lt=5)
    # print(q4)
    # print(q4.query)

    # q5 = Post.objects.filter(id__lte=5)
    # print(q5)
    # print(q5.query)

    # q5 = Post.objects.filter(title__istartswith='b')
    # print(q5)
    # print(q5.query)


    # q6 = Post.objects.filter(title__endwith='b')
    # print(q6)
    # print(q6.query)


    # q7 = Post.objects.order_by('private')

    # w = q7.exclude(title__istartswith='b')
    # print(w)
    # print(w.query)

    # q6 = Post.objects.filter(title__endswith='b')
    # print(q6)
    # print(q6.query)


    # q7 = Post.objects.annotate(private_posts=Count('private'))
    # print(q7)
    # print(q7.query)
    # for x in q7[:5]:
    #     print(x.private_posts)

    # q8 = Post.objects.order_by('id').reverse()
    # print(q8)
    # print(q8.query)


    # q8 = Post.objects.order_by('user_id').distinct('user_id')
    # print(q8)
    # print(q8.query)


    # q9 = Post.objects.values('user_id','private')
    # print(q9[:3])
    # # print(q9.query)

    # q10 = Post.objects.values_list('user_id','private')
    # print(q10[:3])
    # <QuerySet [{'user_id': 1, 'private': True}, {'user_id': 1, 'private': False}, {'user_id': 1, 'private': False}]>
    # # print(q10.query)

    # q11 = Post.objects.values_list('id')
    # print(q11[:3])
    # <QuerySet [(1, True), (1, False), (1, False)]>
    # # print(q11.query)

    # q11 = Post.objects.values_list('id',flat=True)
    # print(q11[:3])
    # <QuerySet [1, 2, 3]>
    # # print(q11.query)


    # q11 = Post.objects.values_list('id',flat=True)
    # print(q11[:3])
    # # print(q11.query)

    # Post.objects.filter(private=True)



    # q12 = Post.objects.filter(private=True)
    # print(q12[:3])

    # method define in model manager
    # q13 = Post.objects.public_post()
    # print(q13[:3])


    # q14 = Post.objects.get_total_public_post()
    # print(q14)


    # q15 = Post.objects.order_by('user_id').values('user_id','id').annotate(id_count=Count('id'))
    # print(q15)
    # # print(q15.query)

    # q15 = Post.objects.values('user_id').order_by('user_id').annotate(id_count=Count('id'))
    # print(q15)
    # print(q15.query)


    # q16 = Post.objects.filter(user__first_name__contains='W')
    # print(q16)
    # print(q16.query)


    # q17 = Post.objects.filter(user__profile__name__contains='W')
    # print(q17)
    # print(q16.query)

    # q15 = Post.objects.annotate(name=F('user__first_name')).values('name').order_by('user_id').annotate(id_count=Count('id'))
    # print(q15)
    # print(q15.query)

    # q16 = Post.objects.filter(
    #     Q(title__startswith='t') | Q(title__endswith='q') | Q(user__in=[2,3,4])
    # )
    # print(q16)
    # print(q16.query)


def lean_query_date():
    # q1 = Post.objects.filter(created__year='2020')
    # print(q1)
    # print(q1.query)

    # q1 = Post.objects.filter(created__year='2022',created__month='2')
    # print(q1)
    # print(q1.query)

    # q1 = Post.objects.filter(created__year__lte='2022')
    # print(q1)
    # print(q1.query)

    # q1 = Post.objects.filter(created__year__lte='2022',created__day='1')
    # print(q1)
    # print(q1.query)

    # q1 = Post.objects.filter(created__year__lte='2022',created__day='1')
    # print(q1)
    # print(q1.query)
    now = timezone.now()
    print(now)
    # print(now.year)
    # print(now.month)
    # print(now.day)
    # print(now.hour)

    # q5 = Post.objects.filter(created__year=now.year,created__month=now.month)
    # print(q5)
    # print(q5.query)

    e = now.replace(hour=0,minute=0,second=0,microsecond=0)
    print(e)
    after2hour = now + timedelta(hours=2)
    print('time after 2 hours',after2hour)

    din_ka_suruwat_ka_time = now.replace(hour=0,minute=0,second=0,microsecond=0)
    print(din_ka_suruwat_ka_time)
    agle_din_ka_suruwat_ka_time = din_ka_suruwat_ka_time + timedelta(days=1)
    print(agle_din_ka_suruwat_ka_time)


    # q7 = Post.objects.filter(created__gte=din_ka_suruwat_ka_time,created__lt=agle_din_ka_suruwat_ka_time)
    # print(q7)
    # print(q7.query)


    q8 = Post.objects.filter(created__year=now.year,created__month=now.month,created__day=now.day)
    print(q8)
    # print(q7.query)

    





if __name__ == '__main__':
    # autopip8 will shift this to up so imorting here as it should be after django setup
    from user.models import CustomUser
    from post.models import Post
    from user.models import Profile
    from django.contrib.auth.hashers import make_password
    from django.db.models import Count, Sum, F, Q 
    # learn_query()
    lean_query_date()
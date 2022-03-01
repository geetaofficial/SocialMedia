from xmlrpc.client import boolean
import django
import os
from faker import Faker
import random
import warnings
from django.utils import timezone
from dateutil import relativedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialMedia.settings')
django.setup()


def user_data(ne=10):
    print('filling users')
    for _ in range(ne):
        f = Faker('en_US')
        # nb=random.randrange(12, 20)
        data = {
            "email": f.email(),
            "first_name": f.first_name(),
            "last_name": f.last_name(),
            "username": f.email(),
            "password": make_password(f.email()),
        }
        # with warnings.catch_warnings():
        #     warnings.simplefilter("ignore")
        CustomUser.objects.create(**data)

    print(f'{ne} data filled')


def post_data(ne=100):
    print('filling posts')
    ul = list(CustomUser.objects.all())
    for _ in range(ne):
        f = Faker('en_US')
        nb = random.randrange(12, 20)
        data = {
            "title": f.sentence(nb_words=nb),
            "caption": f.sentence(nb_words=nb),
            "user": random.choice(ul),
        }

        Post.objects.create(**data)

    print(f'{ne} data filled')


def user_post_data(email, ne=50):
    print(f'filling user {email} posts')
    user = CustomUser.objects.get(email=email)
    for _ in range(ne):
        f = Faker('en_US')
        nb = random.randrange(12, 20)
        data = {
            "title": f.sentence(nb_words=nb),
            "caption": f.sentence(nb_words=nb),
            "user": user,
            "private": random.choice([True, False]),
        }

        Post.objects.create(**data)

    print(f'{ne} data filled')


def last_one_month_post():
    # now = timezone.now()
    tt = timezone.now()
    current_month = tt.replace(hour=0, minute=0, second=0, microsecond=0)
    print(current_month)
    previus_month = current_month - relativedelta.relativedelta(months=1)
    print(previus_month)
    one_month_post = Post.objects.filter(created__year__gte=previus_month.year,
                                         created__month__gte=previus_month.month,
                                         created__year__lte=current_month.year,
                                         created__month__lte=current_month.month,
                                         )
    print(one_month_post.query)
    print(one_month_post)



def get_odd():
    l = range(1,51)
    odd_l = list(filter(lambda x:x%2!=0,l))
    return odd_l





if __name__ == '__main__':
    # autopip8 will shift this to up so imorting here as it should be after django setup
    from user.models import CustomUser
    from post.models import Post
    from user.models import Profile
    from django.contrib.auth.hashers import make_password
    # python manage.py createsuperuser --email geeta@gmail.com --username geeta@gmail.com
    # user_data(50)
    post_data()
    # post_data()
    # lead_data3()
    # user_post_data('geeta@gmail.com')
    # last_one_month_post()
    # otp = get_otp()
    # print(otp)
    odd_n = get_odd()
    print(odd_n)



# s1 = list();
# for i in range(0, 49):
#    s1[i] = i

# print(s1)
#  l = range(50)

# # if not (s1%2==0):
# #     print(s1)




    

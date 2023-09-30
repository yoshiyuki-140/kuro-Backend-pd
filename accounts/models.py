from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Accounts(AbstractUser):
    # 名前フィールド
    name = models.CharField('ニックネーム',max_length=100)
    birth_date = models.DateField('誕生日')
    email = models.EmailField('Email',max_length=100)
    password = models.CharField('パスワード',max_length=100)
    region = models.CharField('地域',max_length=100)
    Profession = models.CharField('職業',max_length=100)

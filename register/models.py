#-*- coding:utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.core.exceptions import ValidationError

from captcha.fields import CaptchaField

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def validate_studentid(value):
    if (len(value)!=10) or ( not value.isdigit()):
        raise ValidationError('not correct!')

def validate_phone(value):
    if ((len(value)!=11)and(len(value)!=6)) or ( not value.isdigit()):
        raise ValidationError('not correct!')

def validate_chinese(value):
    #python2

    if len(value)<2 :
        raise ValidationError('please input Chinese !')
    for ch in value :
        a=ch.decode('utf-8')
        if a<u'\u4e00' or a>u'\u9fff':
            raise ValidationError('please input Chinese')


class UserProfile(models.Model):
    def __str__(self):
        return self.name

    user = models.ForeignKey(User)
    name = models.CharField(max_length=5,validators=[validate_chinese,])
    
    cellphone = models.CharField(max_length=11,validators=[validate_phone,])

class UserProfileForm(ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = UserProfile
        fields=('name','cellphone')

class UserForm(UserCreationForm):
    username=forms.CharField(max_length=10,validators=[validate_studentid,])



class GroupProfile(models.Model):
    def __str__(self):
        return self.user.username

    user=models.ForeignKey(User)

    name1 = models.CharField(max_length=5,validators=[validate_chinese,])
    studentid1 = models.CharField(max_length=10,validators=[validate_studentid])
    phone1 = models.CharField(max_length=11,validators=[validate_phone,])

    name2 = models.CharField(max_length=5,validators=[validate_chinese])
    studentid2 = models.CharField(max_length=10,validators=[validate_studentid])
    phone2 = models.CharField(max_length=11,validators=[validate_phone,])

class GroupForm(ModelForm):

    captcha =CaptchaField()
    class Meta:
        model = GroupProfile
        fields=('name1','studentid1','phone1','name2','studentid2','phone2')

class GroupUserForm(UserCreationForm):
    pass
#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/3/8
# @Author: Lingchen
# @Prescription: 创建表单.
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """ 包含一个内嵌的Meta类,创建表单."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

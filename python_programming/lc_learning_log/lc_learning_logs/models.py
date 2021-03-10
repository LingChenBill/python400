from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 在代码层面,模型就是一个类,就像前面讨论的每个类一样,包含属性和方法.
# 表示用户将要存储的主题的模型.


class Topic(models.Model):
    """ 用户学习的主题. """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ 返回模型的字符串表示. """
        return self.text


class Entry(models.Model):
    """ 学到的有关某个主题的具体知识.
        多对一关系.
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta存储用于管理模型的额外信息. """
        verbose_name_plural = 'entries'

    def __str__(self):
        """ 返回模型的字符串表示. """
        return self.text[:50] + "..."

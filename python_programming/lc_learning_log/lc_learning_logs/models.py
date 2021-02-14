from django.db import models

# Create your models here.
# 在代码层面,模型就是一个类,就像前面讨论的每个类一样,包含属性和方法.
# 表示用户将要存储的主题的模型.


class Topic(models.Model):
    """ 用户学习的主题. """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ 返回模型的字符串表示. """
        return self.text

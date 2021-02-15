from django.shortcuts import render

from .models import Topic
# Create your views here.


def index(request):
    """ 学习笔记的主页. """
    return render(request, 'lc_learning_logs/index.html')


def topics(request):
    """ 显示所有的主题. """
    my_topics = Topic.objects.order_by('date_added')
    context = {'topics': my_topics}
    return render(request, 'lc_learning_logs/topics.html', context)


def topic(request, topic_id):
    """ 显示单个主题及其所有的条目. """
    my_topic = Topic.objects.get(id=topic_id)
    # date_added前面的-号指定按降序排序.
    entries = my_topic.entry_set.order_by('-date_added')
    context = {'topic': my_topic, 'entries': entries}
    return render(request, 'lc_learning_logs/topic.html', context)

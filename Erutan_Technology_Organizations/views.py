from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.


def index(request):
    # The home page of ...
    return render(request, 'Erutan_Technology_Organizations/index.xhtml')


def topics(request):
    # Show all topics.
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'Erutan_Technology_Organizations/topics.xhtml', context)


def topic(request, topic_id):
    # Show a single topic and all its entries.
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'Erutan_Technology_Organizations/topic.xhtml', context)


def new_topic(request):
    # 添加新主题
    if request.method != 'POST':
        # 未提交数据:创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('Erutan_Technology_Organizations:topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'Erutan_Technology_Organizations/new_topic.xhtml', context)


def new_entry(request, topic_id):
    # 在特定的主题中添加新条目
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据:创建一个新表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('Erutan_Technology_Organizations:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'Erutan_Technology_Organizations/new_entry.xhtml', context)


def edit_entry(request, entry_id):
    # 编辑既有条目
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求,使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Erutan_Technology_Organizations:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'Erutan_Technology_Organizations/edit_entry.xhtml', context)

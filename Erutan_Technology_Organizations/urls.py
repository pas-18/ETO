# -*- coding: utf-8 -*-
from django.urls import path, re_path
from . import views
app_name = 'Erutan_Technology_Organizations'
urlpatterns = [
    # Home page
    path("", views.index, name='index'),
    # page that shows all topics.
    path("topics/", views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
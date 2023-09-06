from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('runtest/', runtest, name='runtest'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('question/<int:ques_id>/', show_question_info, name='question'),
    path('category/<int:cat_id>/', show_category, name='category'),

]
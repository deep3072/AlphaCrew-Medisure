
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'acrew'


urlpatterns = [

    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^search/$', views.search, name='search'),
    url(r'^hos/$', views.nearby, name='nearby'),
    url(r'^womenshealth/$', views.womenshealth, name='womenshealth'),
    url(r'^corona/$', views.corona, name='corona'),
    url(r'^exercise/$', views.exercise, name='exercise'),
    url(r'^diseases/$', views.diseases, name='diseases'),

    url(r'^symptoms/acrew/flu/$', views.flu, name='flu'),
    url(r'^symptoms/acrew/cough/$', views.cough, name='cough'),
    url(r'^symptoms/acrew/fever/$', views.fever, name='fever'),
    url(r'^symptoms/acrew/Jaundice/$', views.jaundice, name='jaundice'),
    url(r'^symptoms/acrew/diabetes/$', views.diabetes, name='diabetes'),
    url(r'^symptoms/acrew/malaria/$', views.malaria, name='malaria'),
    url(r'^symptoms/acrew/bloodpressure/$', views.bloodpressure, name='bloodpressure'),
    url(r'^symptoms/acrew/allergies/$', views.allergies, name='allergies'),
    url(r'^symptoms/acrew/typhoid/$', views.typhoid, name='typhoid'),
    url(r'^symptoms/acrew/stomachache/$', views.stomachache, name='stomachache'),
    url(r'^symptoms/acrew/conjuctivitis/$', views.conjuctivitis, name='conjuctivitis'),
    url(r'^symptoms/acrew/dengue/$', views.dengue, name='dengue'),
    url(r'^symptoms/$', views.symptoms, name='symptoms'),

    # url(r'^quiz_world/$', views.quiz_world, name='quiz_world'),
    # path('quiz_world/<course_name>/', views.quizview),

]

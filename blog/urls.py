from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('article/<int:article_id>/', views.show_article, name='article'),

    path('labsix/', views.labSix, name='labsix'),
]
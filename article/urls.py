from django.contrib import admin
from django.urls import path, include
from .import views
#from article.views import RSSFeed


app_name='article'
urlpatterns = [
 	path('', views.index, name='index'),
   # path('list', views.list, name='list'),// now in use right now.
    path('<int:id>/', views.detail, name='detail'),
    path('test', views.test, name='test'),
   # path('feed', RSSFeed(), name = 'RSS'), #Not working

]
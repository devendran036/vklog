from django.urls import path,include
from django.conf.urls import url
from home import views
urlpatterns = [path('',views.homee),path('about',views.about),path('contact',views.contact),path('price',views.price),path('service',views.service)]

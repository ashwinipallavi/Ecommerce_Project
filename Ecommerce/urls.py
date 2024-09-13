from django.contrib import admin
from django.urls import path

from zay import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index, name='home'),
    path('about',views.about, name='about'),
    path('shop',views.shop, name='shop'),
    path('contact',views.contact, name='contact'),
]
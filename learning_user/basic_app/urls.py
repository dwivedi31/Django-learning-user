from django.urls import path
from . import views

#templating urls!
app_name = 'basic_app'

urlpatterns = [
    path('', views.index,name='index'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/',views.logout,name='logout'),
    path('special/',views.special,name='special')
]

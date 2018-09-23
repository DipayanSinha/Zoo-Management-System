from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = "home"),
    path('login/',views.login_user,name = "login"),
    path('logout/',views.logout_user,name ="logout"),
    path('add_department',views.add_department,name='add_department'),
    path('add_exhibit',views.add_exhibit,name='add_exhibit'),
    path('add_animal',views.add_animal,name='add_animal'),
    path('add_staff',views.add_staff,name = 'add_staff')

]

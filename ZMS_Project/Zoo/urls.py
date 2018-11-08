from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = "home"),
    path('login/',views.login_user,name = "login"),
    path('logout/',views.logout_user,name ="logout"),
    path('add_department',views.add_department,name='add_department'),
    path('add_exhibit',views.add_exhibit,name='add_exhibit'),
    path('add_animal',views.add_animal,name='add_animal'),
    path('add_staff',views.add_staff,name = 'add_staff'),
    path('view_animals',views.view_animals, name = 'view_animals'),
    path('department_list/',views.deptList,name='department_list'),
    path(r'^profile/(?P<id>[0-9]+)/$',views.profile,name='profile'),
    path('sidebar/',views.sidebar,name = 'sidebar'),
    path('test/',views.test,name = 'test'),
    path(r'^delete/(?P<id>[0-9]+)/$',views.delete,name = 'delete'),
    path(r'^edit_department/(?P<id>[0-9]+)/$', views.edit_department, name='edit_department'),
    path('search_department/',views.search_department,name = 'search_department'),

]

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
    path(r'^profile/(?P<id>[0-9]+)/$',views.department_profile,name='department_profile'),
    path('sidebar/',views.sidebar,name = 'sidebar'),
    path('test/',views.test,name = 'test'),
    path(r'^delete/(?P<id>[0-9]+)/$',views.delete,name = 'delete'),
    path(r'^edit_department/(?P<id>[0-9]+)/$', views.edit_department, name='edit_department'),
    path(r'^delete_animal/(?P<id>[0-9]+)/$',views.animal_delete,name = 'animal_delete'),
    path(r'^edit_animal/(?P<id>[0-9]+)/$', views.edit_animal, name='edit_animal'),
    path(r'^animal_profile/(?P<id>[0-9]+)/$',views.animal_profile,name='animal_profile'),
    path(r'^delete_staff/(?P<id>[0-9]+)/$',views.staff_delete,name = 'staff_delete'),
    path(r'^edit_staff/(?P<id>[0-9]+)/$', views.edit_staff, name='edit_staff'),
    path(r'^staff_profile/(?P<id>[0-9]+)/$',views.staff_profile,name='stafff_profile'),
    path('staff_list/',views.view_staff,name='staff_list'),
    path(r'^delete_exhibit/(?P<id>[0-9]+)/$',views.exhibit_delete,name = 'exhibit_delete'),
    path(r'^edit_exhibit/(?P<id>[0-9]+)/$', views.edit_exhibit, name='edit_exhibit'),
    path(r'^exhibit_profile/(?P<id>[0-9]+)/$',views.exhibit_profile,name='exhibit_profile'),
    path('exhibit_list/',views.view_exhibit,name='exhibit_list'),

    #path('search_department/',views.search_department,name = 'search_department'),

]

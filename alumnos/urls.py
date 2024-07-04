#from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('index',views.index, name='index'),

    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos/<int:pk>/edit/', views.alumnos_findEdit, name='alumnos_finEdit'),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),
]
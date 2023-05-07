from django.urls import path

from.import views
urlpatterns = [
    path('hombre/',views.hombre, name='home'),
    path('caballeros/',views.caballeros, name='Caballeros'),
    path('mujer/',views.mujer, name='Mujer'),
    path('create-project/',views.createProject, name='create-project'),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
    path('project/<str:pk>/',views.project, name="proyecto"),
]

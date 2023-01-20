from . import views
from django.urls import path
app_name = 'appTodo'

urlpatterns = [
    path('',views.todo, name='todo'),
    path('delete/<int:task_id>/',views.delete, name='delete'),
    path('update/<int:task_id>/',views.update, name='update'),
    path('cbvhome/', views.listview_task.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.detailview_task.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.updateview_task.as_view(), name='cbvupdate'),
    path('cbvdelete/',views.deleteview_task.as_view(), name='cbvdelete')
]

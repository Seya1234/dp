from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:uid>/', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Detaillistview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>',views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvupdelete/<int:pk>',views.Taskdeleteview.as_view(), name='cbdelete')
]
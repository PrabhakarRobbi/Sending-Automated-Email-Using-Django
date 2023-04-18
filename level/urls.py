from django.urls import path
from . import views 
app_name='level'
urlpatterns =[
    path('',views.Home,name='Home'),
    path('page/',views.Page,name='Page'),
    path('register/', views.register, name="register"),
    path('success/', views.success, name="success"),
    path('message/', views.message, name="message"),
    path('Display/',views.Display,name='Display'),
    path('<int:id>/',views.Update,name='Update'),
    path('delete/<int:id>/',views.delete_data,name='delete_data'),
    path('Conform/',views.Conform,name='Conform'),
    path('python/',views.Python,name='Python'),
    path('Aws/',views.Aws,name='Aws'),
    path('Devops/',views.Devops,name='Devops'),
    path('Java/',views.Java,name='Java'),
    path('Cloud/',views.Cloud,name='Cloud')
]
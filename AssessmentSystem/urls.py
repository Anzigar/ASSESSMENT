from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signup, name='signup'),
    path('signup',views.signup, name='signup'),
    path('manageuser',views.manageuser, name='manageuser'),
    path('edituser/<str:pk>',views.edituser, name='edituser'),
    path('deleteuser/<str:pk>',views.deleteuser, name='deleteuser'),
    path('adduser',views.adduser, name='adduser'),
    path('index', views.index, name='index'),
    path('main',views.main, name='main'),
    path('addproject',views.addproject, name='addproject'),
    path('addexp', views.addexp, name='addexp'),
    path('deleteproject/<str:pk>',views.deleteproject, name='deleteproject'),
    path('manageexp', views.manageexp, name='manageexp'),
    path('expensesreport', views.expensesreport, name='expensesreport'),
    path('manageproject', views.manageproject, name='manageproject'),
    #path('editproject/<str:pk>',views.editproject, name='editproject'),
    path('profit', views.profit, name='profit'),
    path('report', views.report, name='report'),
    path('login', views.login, name='login'),
    path('logout',views.logout, name='logout' ),
    path('managerole',views.managerole, name='managerole'),
    path('addrole',views.addrole, name='addrole'),
    path('editrole/<str:pk>',views.editrole, name='editrole'),
    path('grantRole/<str:pk>',views.grantRole, name='grantRole'),
    path('deleterole/<str:pk>',views.deleterole, name='deleterole'),
    path('trash',views.trash, name='trash'),
    
]
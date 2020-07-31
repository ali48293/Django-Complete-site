from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="homePage"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("devs/",views.devs,name="devs"),
    path("<int:id>/",views.devs,name="update"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("devsList/",views.devs_list,name="devsList"),
    
]

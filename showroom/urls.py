from django.urls import path
from . import views
urlpatterns = [
    path('',views.cars,name='cars'),
    path("contact",views.contact,name='contact'),
    path("about",views.about,name='about'),
    path("login",views.login,name='login'),
    path("register",views.register,name='register'),
    path("logout",views.logout,name='logout'),
    path("search",views.search,name='search'),
    path("shop",views.shop,name='shop'),
]

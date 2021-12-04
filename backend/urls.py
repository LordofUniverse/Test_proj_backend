"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backendapp import views


router = routers.DefaultRouter()
router.register(r'userslist', views.ListUsersView, 'userslist')
router.register(r'subslist', views.ListSubscriptionsView, 'subslist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/login/', views.UserLoginView.as_view()),
    path('api/signup/', views.UserSignupView.as_view()),
    path('api/update/', views.UserUpdateSubs.as_view()),
    path('api/check/', views.UserCheckLogin.as_view()),
    path('subslist2/', views.ListSubscriptionsView2.as_view()),
]

from django.urls import include, path
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'userslist', views.ListUsersView(), 'userslist')

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.ListUsersView.as_view(), name='listusers'),
]

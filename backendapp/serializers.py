from django.db.models import fields
from rest_framework import serializers
from .models import User, Subscriptions


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'number', 'password', 'subs')


class SubsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ('title', 'detail', 'image', 'price')


class SubsListSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', )


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'number')


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class SendSubsWhenLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ('title', 'detail', 'image')


class UserUpdateSubsSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    condition = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'title', 'condition')


class UserCheckLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')

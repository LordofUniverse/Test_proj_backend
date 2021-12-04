from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Subscriptions
from .serializers import *

import bcrypt


class ListUsersView(viewsets.ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class ListSubscriptionsView(viewsets.ModelViewSet):
    serializer_class = SubsListSerializer
    queryset = Subscriptions.objects.all()


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            emai = serializer.data.get('email')
            pwd = serializer.data.get('password')

            loginqueryset = User.objects.filter(email=emai, password=pwd)

            if loginqueryset.exists():

                room = User.objects.get(email=emai, password=pwd)
                hashed = bcrypt.hashpw(
                    pwd.encode('utf-8'), bcrypt.gensalt(16))

                subs = room.subs.split(',')

                data = {}
                num = 0

                result = Subscriptions.objects.all()
                for i in result:
                    if i.title in subs:
                        data[num] = {'title': i.title,
                                     'detail': i.detail, 'image': i.image, 'taken': 'yes'}
                    else:
                        data[num] = {'title': i.title,
                                     'detail': i.detail, 'image': i.image, 'taken': 'no'}
                    num += 1

                data['email'] = emai
                data['password'] = hashed

                return Response({'Data': data}, status=status.HTTP_202_ACCEPTED)

            else:
                return Response({'msg': 'It doesnt exists.'}, status=status.HTTP_226_IM_USED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class UserSignupView(APIView):
    serializer_class = UserSignupSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            nam = serializer.data.get('name')
            emai = serializer.data.get('email')
            pwd = serializer.data.get('password')
            num = serializer.data.get('number')

            signupqueryset = User.objects.filter(email=emai)

            if signupqueryset.exists():

                return Response({'Data': 'Email already exists'}, status=status.HTTP_226_IM_USED)

            else:

                room = User(name=nam, email=emai, password=pwd, number=num)
                room.save()

                hashed = bcrypt.hashpw(
                    pwd.encode('utf-8'), bcrypt.gensalt(16))

                return Response({'Data': {'email': emai, 'password': str(hashed)}}, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class ListSubscriptionsView2(APIView):
    serializer_class = SubsListSerializer2

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            emai = serializer.data.get('email')

            updatequeryset = User.objects.filter(email=emai)

            if updatequeryset.exists():
                result = []
                subs = User.objects.get(email=emai).subs.split(',')
                subslist = Subscriptions.objects.all()
                for i in subslist:
                    if i.title in subs:
                        result.append({
                            'title': i.title,
                            'detail': i.detail,
                            'image': i.image,
                            'price': i.price,
                            'bought': 'yes'
                        })
                    else:
                        result.append({
                            'title': i.title,
                            'detail': i.detail,
                            'image': i.image,
                            'price': i.price,
                            'bought': 'no'
                        })

                return Response({'Data': result}, status=status.HTTP_200_OK)

            else:
                return Response({'Data': 'Email doesn"t exists'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateSubs(APIView):
    serializer_class = UserUpdateSubsSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            tit = serializer.data.get('title')
            emai = serializer.data.get('email')
            cond = serializer.data.get('condition')

            updatequeryset = User.objects.filter(email=emai)

            if updatequeryset.exists():

                updatedata = User.objects.get(email=emai)

                if cond == 'yes':
                    if updatedata.subs == '':
                        updatequeryset.update(subs=tit)
                    else:
                        updatequeryset.update(subs=updatedata.subs+','+tit)

                else:
                    subs = updatedata.subs.split(',')
                    final = ''
                    for i in subs:
                        if i != tit:
                            final += i + ','
                    updatequeryset.update(subs=final[:len(final)-1])

                return Response({'Data': 'success'}, status=status.HTTP_200_OK)

            else:
                return Response({'Data': 'Email doesn"t exists'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class UserCheckLogin(APIView):
    serializer_class = UserCheckLoginSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            emai = serializer.data.get('email')
            pwd = serializer.data.get('password')

            updatequeryset = User.objects.filter(email=emai)

            if updatequeryset.exists():
                updatedata = User.objects.get(email=emai)

                if bcrypt.checkpw(updatedata.password.encode('utf-8'), pwd.encode('utf-8')):
                    return Response({'Data': 'yes'}, status=status.HTTP_200_OK)
                else:
                    return Response({'Data': 'no'}, status=status.HTTP_200_OK)

            else:
                return Response({'Data': 'Email doesn"t exists'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

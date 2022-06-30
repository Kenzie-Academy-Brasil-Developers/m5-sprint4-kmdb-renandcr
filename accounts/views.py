from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from permissions.admin_permission import CustomAdminPermission

from accounts.models import User
from accounts.serializers import UserSerializer
from accounts.serializers import UserLoginSerializer

class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_instance = User.objects.get(email=serializer.data["email"])
        user_dict = serializer.data.copy()

        user_dict["date_joined"] = user_instance.__dict__["date_joined"].isoformat()
        user_dict["updated_at"] = user_instance.__dict__["updated_at"].isoformat()

        return Response(user_dict, status.HTTP_201_CREATED)


class LoginUsers(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user_instance = authenticate(
            email = serializer.validated_data["email"],
            password = serializer.validated_data["password"],
        )

        if user_instance:
            token, _ = Token.objects.get_or_create(user=user_instance)

            return Response({"token": token.key})

        return Response(
            {"detail": "Invalid email or password"}, status.HTTP_401_UNAUTHORIZED
        )

class ListAllUsers(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomAdminPermission]
    def get(self, request):
        all_users = User.objects.all()
        result_page = self.paginate_queryset(all_users, request, view=self)
        serializer = UserSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

class ListUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomAdminPermission]
    def get(self, _, user_id):
        user_instance = get_list_or_404(User, id=user_id)[0]
        serializer = UserSerializer(user_instance)

        return Response(serializer.data)


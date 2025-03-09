from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import User
from .serializers import UserSerializer  # Adicionando a importação aqui

class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = UserPagination

    def get(self, request):
        users = User.objects.all().order_by('-created_at')
        paginator = self.pagination_class()
        paginated_users = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDetailUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'nick'

    def get_object(self, nick):
        return get_object_or_404(User, pk=nick)

    def get(self, request, nick):
        user = self.get_object(nick)
        return Response(UserSerializer(user).data)

    def put(self, request, nick):
        user = self.get_object(nick)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, nick):
        user = self.get_object(nick)
        user.delete()
        return Response(
            {"message": "Usuário excluído com sucesso"},
            status=status.HTTP_204_NO_CONTENT
        )

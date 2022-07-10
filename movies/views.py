
from rest_framework.pagination import PageNumberPagination 
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework import status

from permissions.admin_permission import CustomAdminPermission
from rest_framework.authentication import TokenAuthentication
from permissions.read_only import ReadOnly 

from movies.serializers import MovieSerializer 
from movies.models import Movie

class CreateListAllMovies(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomAdminPermission|ReadOnly]
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        movies_list = Movie.objects.all()
        result_page = self.paginate_queryset(movies_list, request, view=self)
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

class ListUpdateDeleteMovie(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomAdminPermission|ReadOnly]
    def get(self, _, movie_id):
        movie_instance = get_list_or_404(Movie, id=movie_id)[0]
        serializer = MovieSerializer(movie_instance)

        return Response(serializer.data)
        
    def patch(self, request, movie_id):
        movie_instance = get_list_or_404(Movie, id=movie_id)[0]
        serializer = MovieSerializer(movie_instance, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, _, movie_id): 
        movie_instance = get_list_or_404(Movie, id=movie_id)[0]
        movie_instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)






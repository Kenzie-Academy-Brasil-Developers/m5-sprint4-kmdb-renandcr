from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_list_or_404

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import CustomPermissionToDelete

from .models import Review
from movies.models import Movie
from .serializers import ReviewSerializer


class CreateListAllMovieReview(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, movie_id):
        movie_instance = get_list_or_404(Movie, pk=movie_id)[0]

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie=movie_instance, user=request.user)

        review_dict = serializer.data.copy()
        review_dict["critics"] = {
            "id": request.user.id, 
            "first_name": request.user.first_name, 
            "last_name": request.user.last_name
        }

        return Response(review_dict, status.HTTP_201_CREATED)

    def get(self, request, movie_id):
        review_list = get_list_or_404(Review, movie_id=movie_id)
        result_page = self.paginate_queryset(review_list, request, view=self)
        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

class DeleteReview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermissionToDelete]
    def delete(self, _, review_id):
        review_instance = get_list_or_404(Review, id=review_id)[0]
        review_instance.delete()

        return Response(status.HTTP_204_NO_CONTENT)

class ListAllReviews(APIView, PageNumberPagination):
    def get(self, request):
        review_list = Review.objects.all()
        result_page = self.paginate_queryset(review_list, request, view=self)
        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
   
    

        
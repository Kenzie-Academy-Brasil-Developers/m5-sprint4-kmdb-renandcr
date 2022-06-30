from rest_framework import permissions
from reviews.models import Review
from django.shortcuts import get_list_or_404

class CustomPermissionToDelete(permissions.BasePermission):
    def has_permission(self, request, _):
        review_parameter_id = request.__dict__["parser_context"]["kwargs"]["review_id"]
        review_instance = get_list_or_404(Review, pk=review_parameter_id)[0] 

        return request.user.id == review_instance.user.id or request.user.is_superuser

    

   


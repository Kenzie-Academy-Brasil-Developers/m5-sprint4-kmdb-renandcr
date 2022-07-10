from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields = ["id", "stars", "review", "spoilers", "recomendation", "movie_id"]
        extra_kwargs = {
            "stars": {"max_value": 10, "min_value": 1},
            "user": {"read_only": True},
        }


    def create(self, validated_data):
        user_instance = validated_data.pop("user")
        movie_instance = validated_data.pop("movie")

        return Review.objects.create(**validated_data, movie=movie_instance, user=user_instance)





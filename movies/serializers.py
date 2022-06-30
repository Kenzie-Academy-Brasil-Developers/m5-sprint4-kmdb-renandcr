from rest_framework import serializers
from genres.serializers import GenreSerializer
from genres.models import Genre
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()

    genres = GenreSerializer(many=True)


    def create(self, validated_data):
        genres_list = validated_data.pop("genres")
        movie_instance = Movie.objects.create(**validated_data)

        for item in genres_list:
            genre_instance = Genre.objects.get_or_create(**item)[0]
            genre_instance.movies.add(movie_instance)
                
        return movie_instance

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key != "genres":
                setattr(instance, key, value)
            
            else:
                for item in validated_data["genres"]:
                    try:
                        genre_instance = Genre.objects.get_or_create(**item)[0]
                        genre_instance.movies.add(instance)
                    except:
                        pass

        instance.save()
        return instance
        




 
from rest_framework import serializers
from .models import Movie, Director, Review


class DirectorSerializer(serializers.ModelSerializer):
    amount_movies = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['name', 'amount_movies']

    def get_amount_movies(self, obj):
        return obj.movies.count()



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)
    review_mean = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['title', 'director', 'reviews', 'description', 'duration', 'review_mean']

    def get_review_mean(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            summ = sum(i.star for i in reviews)
            mean = round(summ / len(reviews), 1)
            return mean

class MovieValidationSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(pk=director_id)
        except Director.DoesNotExist:
            raise serializers.ValidationError('Director does not exist')
        return director_id

class ReviewValidationSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    movie_id = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            raise serializers.ValidationError('Movie does not exist')
        return movie_id

class DirectorValidationSerializer(serializers.Serializer):
   name = serializers.CharField()








from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Director, Review
from .serializers import (MovieSerializer, MovieValidationSerializer,
                          DirectorSerializer, DirectorValidationSerializer,
                          ReviewSerializer, ReviewValidationSerializer)
from rest_framework.viewsets import ModelViewSet


class Directorview(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def create(self, request, *args, **kwargs):
        serializer = DirectorValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get['name']
        director = Director.objects.create(name=name)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        director = self.get_object()
        serializer = DirectorValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director.name = serializer.validated_data.get['name']
        director.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MovieView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['title']
        description = serializer.validated_data['description']
        duration = serializer.validated_data['duration']
        director_id = serializer.validated_data['director_id']
        Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = MovieValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.save()


class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data['text']
        stars = serializer.validated_data['stars']
        movie_id = serializer.validated_data['movie_id']
        Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        serializer = ReviewValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = serializer.validated_data['text']
        review.stars = serializer.validated_data['stars']

# @api_view(['GET', 'POST'])
# def directors(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = DirectorValidationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         name = serializer.validated_data.get['name']
#         director = Director.objects.create(name=name)
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             director = Director.objects.get(pk=pk)
#         except Director.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = DirectorSerializer(director)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         director = Director.objects.get(pk=pk)
#         serializer = DirectorValidationSerializer(director, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         director.name = serializer.validated_data.get['name']
#         director.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         director = Director.objects.get(pk=pk)
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def movies(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieValidationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         title = serializer.validated_data['title']
#         description = serializer.validated_data['description']
#         duration = serializer.validated_data['duration']
#         director_id = serializer.validated_data['director_id']
#         Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieValidationSerializer(movie, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie.title = serializer.validated_data.get('title')
#         movie.description = serializer.validated_data.get('description')
#         movie.duration = serializer.validated_data.get('duration')
#         movie.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def reviews(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewValidationSerializer(reviews, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         text = serializer.validated_data['text']
#         stars = serializer.validated_data['stars']
#         movie_id = serializer.validated_data['movie_id']
#         Review.objects.create(text=text, stars=stars, movie_id=movie_id)
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             review = Review.objects.get(pk=pk)
#         except Review.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         review = Review.objects.get(pk=pk)
#         serializer = ReviewValidationSerializer(review, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = serializer.validated_data['text']
#         review.stars = serializer.validated_data['stars']
#         review.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         review = Review.objects.get(pk=pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import serializers

class RatingSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    rating = serializers.IntegerField()
    watched = serializers.BooleanField()

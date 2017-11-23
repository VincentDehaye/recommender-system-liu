from rest_framework import serializers

class RatingSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    movie_id = serializers.IntegerField()
    rating = serializers.IntegerField()
    watched = serializers.BooleanField()

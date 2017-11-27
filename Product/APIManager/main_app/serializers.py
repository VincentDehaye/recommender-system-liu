from rest_framework import serializers

class RatingSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    rating = serializers.IntegerField()
    watched = serializers.BooleanField()
    def validate_rating(self, value):
        try:
            if int(value) not in range(1,5):
                raise serializers.ValidationError("Rating needs to be a number between 1 and 5")
            return value
        except:
            raise serializers.ValidationError("Rating need to be a number between 1 and 5")

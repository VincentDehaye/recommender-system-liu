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

class UserSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    gender = serializers.CharField(allow_blank=True)
    occupation = serializers.CharField(allow_blank=True, max_length=30)

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age must be positive.")
        else:
            return value

    def validate_gender(self, value):
        if value in ("Male", "Female", "Unknown"):
            return value
        else:
            raise serializers.ValidationError("Gender must be Male, Female or Unknown")

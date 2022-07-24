from rest_framework import serializers

from showtimes.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())

    class Meta:
        model = Cinema
        fields = "__all__"
        
import datetime

from rest_framework import serializers

from movielist.models import Movie
from showtimes.models import Cinema, Screening


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True,
                                                 queryset=Screening.objects.filter(
                                                     date__lte=datetime.date.today() + datetime.timedelta(days=30)
                                                 ),
                                                 view_name='movies_detail')

    class Meta:
        model = Cinema
        fields = "__all__"


class ScreeningSerializer(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())
    movie = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all())

    class Meta:
        model = Screening
        fields = '__all__'

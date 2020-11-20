
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth.models import User
from apps.webapp.models import Film, Person, Planet, Species
from .serializers import FilmSerializer, PersonSerializer, PlanetSerializer, SpeciesSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Film.objects.all()
        title = self.request.query_params.get('title', None)
        episode_id = self.request.query_params.get('episode_id', None)
        if title:
            queryset = queryset.filter(title__contains=title)
        if episode_id:
            queryset = queryset.filter(episode_id=episode_id)

        return queryset.order_by('film_id')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Person.objects.all()
        home_world = self.request.query_params.get('home_world', None)
        name = self.request.query_params.get('name',None)
        if home_world:
            queryset = queryset.filter(home_world__name__iexact=home_world)
        if name:
            queryset = queryset.filter(name__contains=name)

        return queryset.order_by('person_id')


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Planet.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)

        return queryset.order_by('planet_id')


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Species.objects.all()
        home_world = self.request.query_params.get('home_world', None)
        name = self.request.query_params.get('name',None)
        if home_world:
            queryset = queryset.filter(home_world__name__iexact=home_world)
        if name:
            queryset = queryset.filter(name__contains=name)

        return queryset.order_by('species_id')

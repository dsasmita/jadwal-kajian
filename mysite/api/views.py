
# Create your views here.
from datetime import datetime

from rest_framework import viewsets, permissions

from kajian.models import Schedule, City, Province, Mosque, Ustad
from .serializers import ScheduleSerializer, CitySerializer, ProvinceSerializer, MosqueSerializer, UstadSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Schedule.objects.all().filter(start_from__gte=datetime.now()).order_by('-start_from')
    serializer_class = ScheduleSerializer

class MosqueViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Mosque.objects.all()
    serializer_class = MosqueSerializer

class CityViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class UstadViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Ustad.objects.all()
    serializer_class = UstadSerializer

# Create your views here.
from datetime import datetime

import self as self
from rest_framework import viewsets, permissions
from url_filter.integrations.drf import DjangoFilterBackend

from kajian.models import Schedule, City, Province, Mosque, Ustad
from .serializers import ScheduleSerializer, CitySerializer, ProvinceSerializer, MosqueSerializer, UstadSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title', 'ustad', 'mosque', 'city','start_from']
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

    def get_queryset(self):
        type = self.request.query_params.get('type', None)
        if type is None:
            queryset = Schedule.objects.all().filter(start_from__gte=datetime.now()).order_by('-start_from')
        elif type == 'archive':
            queryset = Schedule.objects.all().order_by('start_from')
        return queryset

class MosqueViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Mosque.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['city']
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
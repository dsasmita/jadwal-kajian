from django.http import HttpResponse
from django.views import generic

from .models import Schedule


class HomeView(generic.ListView):
    template_name = 'kajian/home.html'
    context_object_name = 'latest_schedule_list'

    def get_queryset(self):
        return Schedule.objects.order_by('start_from')[:5]
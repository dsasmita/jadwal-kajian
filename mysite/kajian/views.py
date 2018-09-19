from datetime import datetime
from django.views import generic
from .models import Schedule


class HomeView(generic.ListView):
    template_name = 'kajian/home.html'
    context_object_name = 'schedule_list'

    def get_queryset(self):
        return Schedule.objects.filter(start_from__gte=datetime.now()).order_by('start_from')[:4]

class DetailView(generic.DetailView):
    model = Schedule
    template_name = 'kajian/detail.html'
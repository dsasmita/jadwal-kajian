from datetime import datetime
from django.views import generic
from .models import Schedule, City


class HomeView(generic.ListView):
    template_name = 'kajian/home.html'
    context_object_name = 'schedule_list'

    def get_queryset(self):
        return Schedule.objects.filter(start_from__gte=datetime.now()).order_by('start_from')[:4]

class ListView(generic.ListView):
    template_name = 'kajian/list.html'
    context_object_name = 'schedule_list'

    def get_queryset(self):
        sch = Schedule.objects
        # keyword = self.request.GET.get('keyword') or ''
        city = self.request.GET.get('city') or '0'
        if int(city) != 0:
            sch = sch.filter(city_id=city)

        sch = sch.filter(start_from__gte=datetime.now()).order_by('start_from')

        return sch

    def get_context_data(self, **kwargs):
        keyword = self.request.GET.get('keyword') or ''
        city = self.request.GET.get('city') or '0'

        context = super(ListView, self).get_context_data(**kwargs)

        context['title'] = 'Kajian Terbaru'
        context['city'] = int(city)
        context['keyword'] = keyword
        context['cities'] = City.objects.order_by('name')

        return context

class DetailView(generic.DetailView):
    model = Schedule
    template_name = 'kajian/detail.html'
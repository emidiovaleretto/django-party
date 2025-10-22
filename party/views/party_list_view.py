import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from party.models import Party


class PartyListView(LoginRequiredMixin, ListView):
    '''
    View to list parties hosted by the logged-in user that are scheduled for today or later.
    '''
    template_name = 'party/party_list/page_parties_list.html'
    context_object_name = 'parties'

    def get_queryset(self):
        return Party.objects.filter(
            host=self.request.user,
            party_date__gte=datetime.date.today()
        ).order_by(
            "party_date"
        )

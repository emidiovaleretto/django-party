from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views import View

from django.http import QueryDict
from django.shortcuts import render, get_object_or_404

from party.forms import PartyForm
from party.models import Party


class PartyDetailView(LoginRequiredMixin, DetailView):
    '''
    View to display the details of a specific party.
    '''
    model = Party
    template_name = "party/party_detail/page_party_detail.html"
    pk_url_kwarg = "party_uuid"
    context_object_name = "party"


class PartyDetailPartial(LoginRequiredMixin, View):

    def get(self, request, party_uuid, *args, **kwargs):
        '''
        Handle GET requests for the party detail.
        '''
        party = get_object_or_404(Party, id=party_uuid)
        form = PartyForm(instance=party)

        context = {
            "party": party,
            "form": form
        }

        return render(
            request,
            "party/party_detail/partial_party_edit_form.html",
            context=context
        )

    def put(self, request, party_uuid, *args, **kwargs):
        '''
        Handle PUT requests for updating a party.
        '''
        party = get_object_or_404(Party, id=party_uuid)
        data = QueryDict(request.body).dict()
        form = PartyForm(data, instance=party)

        context = {
            "party": party,
            "form": form
        }

        if form.is_valid():
            form.save()

        return render(
            request,
            "party/party_detail/partial_party_detail.html",
            context=context
        )

from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from party.forms import PartyForm


@login_required
def create_party_view(request):
    '''
    View to create a new party.
    '''
    form = PartyForm()

    if request.method == "POST":
        form = PartyForm(request.POST)

        if form.is_valid():
            party = form.save(commit=False)
            party.host = request.user
            party.save()

            return redirect("page_party_detail", party_uuid=party.id)

    return render(request, "party/new_party/page_new_party.html", {"form": form})


@login_required
def partial_check_party_date(request):
    form = PartyForm(request.GET)
    return HttpResponse(as_crispy_field(form["party_date"]))


@login_required
def partial_check_invitation_note(request):
    form = PartyForm(request.GET)
    return HttpResponse(as_crispy_field(form["invitation_note"]))

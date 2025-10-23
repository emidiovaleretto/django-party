from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

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

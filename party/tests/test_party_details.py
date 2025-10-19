import datetime
from urllib.parse import urlencode

import pytest
from django.urls import reverse

from party.models import Party


@pytest.mark.django_db
def test_party_detail_page_returns_whole_page_with_a_single_party(
    authenticated_client,
    create_user,
    django_user_model,
    create_party,
):
    '''
    Test that the party detail page returns the whole page with a single party's details.
    Given an authenticated user and a created party,
    when the user accesses the party detail page,
    then the response should have a 200 status code and contain the party details in the context
    context.
    '''

    party = create_party(host=create_user)

    url = reverse('page_single_party', args=[party.uuid])
    response = authenticated_client(create_user).get(url)

    assert response.status_code == 200
    assert response.context_data["party"] == party


@pytest.mark.django_db
def test_detail_partial_get_method_returns_a_form_prefilled_with_party_details(
    authenticated_client,
    create_user,
    django_user_model,
    create_party
):
    '''
    Test that the party detail partial GET method returns a form prefilled with party details.
    Given an authenticated user and a created party,
    when the user accesses the party detail partial view via GET,
    then the response should have a 200 status code and contain a form prefilled with the party details.
    '''

    party = create_party(host=create_user)

    url = reverse('partial_party_detail', args=[party.uuid])
    response = authenticated_client(create_user).get(url)

    assert response.status_code == 200
    assert "form" in response.context
    assert response.context["form"].instance == party


@pytest.mark.django_db
def test_detail_partial_put_method_returns_updated_party_details(
    authenticated_client,
    create_user,
    django_user_model,
    create_party
):
    '''
    Test that the party detail partial PUT method returns updated party details.
    Given an authenticated user and a created party,
    when the user submits updated party details via PUT,
    then the response should have a 200 status code and the party details should be updated.
    '''

    party = create_party(host=create_user)

    url = reverse("partial_party_detail", args=[party.uuid])

    data = urlencode({
        "party_date": "2025-06-06",
        "party_time": "18:00:00",
        "venue": "New Venue",
        "invitation_note": "New Invitation Note",
    })

    response = authenticated_client(create_user).put(
        url,
        content_type="application/x-www-form-urlencoded",
        data=data
    )

    assert response.status_code == 200
    assert Party.objects.get(uuid=party.uuid).party_date == datetime.date(2025, 6, 6)
    assert Party.objects.get(uuid=party.uuid).party_time == datetime.time(18, 0, 0)
    assert Party.objects.get(uuid=party.uuid).venue == "New Venue"
    assert Party.objects.get(uuid=party.uuid).invitation_note == "New Invitation Note"

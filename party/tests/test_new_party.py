import pytest
from django.urls import reverse

from party.models import Party


@pytest.mark.django_db
def test_create_party(authenticated_client, create_user):
    '''
    Test creating a new party via the new party page.
    '''
    url = reverse("page_new_party")
    data = {
        "party_date": "2025-12-31",
        "party_time": "20:00:00",
        "venue": "Downtown Club",
        "invitation_note": "Join us for a night of fun!",
    }

    response = authenticated_client(create_user).post(url, data)

    assert response.status_code == 302
    assert Party.objects.count() == 1


def test_create_party_invitation_note_less_than_10_chars_returns_error_message(
    authenticated_client,
    create_user
):
    '''
    Test that creating a new party with an invitation note less than 10 characters
    returns an appropriate error message.
    '''
    url = reverse("page_new_party")
    data = {
        "party_date": "2020-12-31",
        "party_time": "20:00:00",
        "venue": "Downtown Club",
        "invitation_note": "Too short"
    }

    response = authenticated_client(create_user).post(url, data)

    assert not response.context["form"].is_valid()
    assert "You really should write an invitation." in response.content.decode()
    assert Party.objects.count() == 0


def test_create_party_in_past_date_returs_error_message(authenticated_client, create_user):
    '''
    Test that creating a new party with a date in the past
    returns an appropriate error message.
    '''
    url = reverse("page_new_party")
    data = {
        "party_date": "2020-12-31",
        "party_time": "20:00:00",
        "venue": "Downtown Club",
        "invitation_note": "Come to my party and have fun with us!"
    }

    response = authenticated_client(create_user).post(url, data)

    assert not response.context["form"].is_valid()
    assert "You chose a date in the past." in response.content.decode()
    assert Party.objects.count() == 0

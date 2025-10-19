import datetime

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_party_list_page_returns_list_of_users_future_parties(
    authenticated_client,
    create_user,
    create_party,
    django_user_model
):
    '''
    Test that the party list page returns only future parties for the authenticated user.
    1. Create a test user and authenticate.
    2. Create multiple parties for the user: some in the past, some in the future.
    3. Create a party for another user to ensure it is not included.
    4. Access the party list page.
    5. Verify that only the future parties for the authenticated user are returned.
    6. Check that the response status code is 200 (OK).
    7. Assert that the number of parties returned matches the expected count.
    8. Confirm that the returned parties are indeed the future parties created for the user.
    '''

    today = datetime.date.today()
    user = create_user
    other_user = django_user_model.objects.create_user(
        username="otheruser",
        password="otherpassword123",
    )

    # Create parties for the test user
    party1 = create_party(
        host=user,
        party_date=today,
        venue="Venue A"
    )

    party2 = create_party(
        host=user,
        party_date=today + datetime.timedelta(days=30),
        venue="Venue B"
    )

    create_party(
        host=other_user,
        venue="Venue C"
    )
    create_party(
        host=user,
        party_date=today - datetime.timedelta(days=2 * 365),
        venue="Venue D",
    )

    url = reverse("page_party_list")
    response = authenticated_client(user).get(url)

    parties_list = list(response.context_data["parties"])

    assert response.status_code == 200
    assert len(parties_list) == 2
    assert parties_list == [party1, party2]

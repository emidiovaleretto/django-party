from django.urls import path
from . import views

list_parties_urlpatterns = [
    path("", views.PartyListView.as_view(), name="page_party_list"),
]

party_detail_urlpatterns = [
    path("party/<uuid:party_uuid>/", views.PartyDetailView.as_view(), name="page_party_detail"),
    path("party/<uuid:party_uuid>/details/",
         views.PartyDetailPartial.as_view(),
         name="partial_party_detail"),

]

urlpatterns = list_parties_urlpatterns + party_detail_urlpatterns

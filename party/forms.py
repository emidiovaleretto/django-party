import datetime

from django import forms
from django.urls import reverse_lazy
from party.models import Party


class PartyForm(forms.ModelForm):
    '''
    Form for creating or updating a Party instance.
    '''
    class Meta:
        model = Party
        fields = ("party_date", "party_time", "venue", "invitation_note")
        widgets = {
            "party_date": forms.DateInput(attrs={
                "type": "date",
                "hx-get": reverse_lazy("partial_check_party_date"),
                "hx-trigger": "blur",
                "hx-swap": "outerHTML",
                "hx-target": "#div_id_party_date"
            }),
            "party_time": forms.TimeInput(attrs={
                "type": "time",
            }),
            "venue": forms.TextInput(attrs={
                "class": "w-full border border-gray-300 rounded-md p-2 my-2",
            }),
            "invitation_note": forms.Textarea(attrs={
                "class": "w-full resize-none border border-gray-300 rounded-md p-2 my-2",
                "hx-get": reverse_lazy("partial_check_invitation_note"),
                "hx-trigger": "blur",
                "hx-swap": "outerHTML",
                "hx-target": "#div_id_invitation_note"
            })
        }

    def clean_invitation_note(self):
        '''
        Ensure that the invitation note is at least 10 characters long.
        '''
        invitation_note = self.cleaned_data["invitation_note"]

        if len(invitation_note) < 10:
            raise forms.ValidationError("You really should write an invitation.")

        return invitation_note

    def clean_party_date(self):
        '''
        Ensure that the party date is not in the past.
        '''
        party_date = self.cleaned_data["party_date"]

        if datetime.date.today() > party_date:
            raise forms.ValidationError("You chose a date in the past.")

        return party_date

from django import forms
from party.models import Party


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ("party_date", "party_time", "venue", "invitation_note")
        widgets = {
            "party_date": forms.DateInput(attrs={
                "type": "date"
            }),
            "party_time": forms.TimeInput(attrs={
                "type": "time"
            }),
            "invitation_note": forms.Textarea(attrs={
                "class": "w-full resize-none",
            })
        }

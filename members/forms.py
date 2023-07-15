from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["firstname", "lastname", "phone", "joined_date"]
        labels = {'firstname': "First name", "lastname": "Last Name","phone": "Mobile Number","joined_date": "Join Date",}
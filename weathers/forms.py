from django import forms


class NameForm(forms.Form):
    city = forms.CharField(max_length=20, min_length=3)
    country = forms.CharField(max_length=50, min_length=3)
    coordination_x = forms.FloatField(min_value=0, max_value=120)
    coordination_y = forms.FloatField(min_value=0, max_value=120)


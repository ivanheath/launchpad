from django import forms
import datetime

class maintform(forms.Form):
    maintname = forms.CharField(label="maintenance name")
    maintticket = forms.CharField(label="ticket for maintenance")
    maintlink = forms.CharField(label="link to ticket")
    maintcompany = forms.CharField(label="company")
    mainttime = forms.DateTimeField(label="maintenance time", widget=forms.DateTimeInput(), initial=datetime.datetime.now())

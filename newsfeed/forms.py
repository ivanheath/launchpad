from django import forms

class newspost(forms.Form):
    newstitle = forms.CharField(label="news title")
    newstext = forms.CharField(label="news")



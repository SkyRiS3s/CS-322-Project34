from django import forms
from blog.models import Listing


class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing



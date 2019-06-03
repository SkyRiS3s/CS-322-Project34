from django import forms
from .models import *


"""
class AddListingForm(forms.Form):
    property_type = forms.ModelChoiceField(queryset=Property.objects.all(),required=False)
    policy = forms.ModelChoiceField(queryset=Cancellation.objects.all(), required=False)
    bed_type = forms.ModelChoiceField(queryset=Beds.objects.all(), required=False)
    room_type = forms.ModelChoiceField(queryset=Rooms.objects.all(), required=False)
    host_id = forms.IntegerField(required=False)
    neighborhood = forms.ModelChoiceField(queryset=Neighborhoods.objects.all(), required=False)
    listing_url = forms.CharField(max_length=200, required=False)
    name = forms.CharField(max_length=200, required=False)
    square_feet = forms.FloatField(required=False)
    summary = forms.CharField(widget=forms.Textarea, required=False)
    space = forms.CharField(widget=forms.Textarea, required=False)
    accomodates = forms.IntegerField(required=False)
    price = forms.FloatField(required=False)
    review_scores_accuracy = forms.FloatField(required=False)
    review_scores_rating = forms.FloatField(required=False)
    review_scores_cleanliness = forms.FloatField(required=False)
    review_scores_location = forms.FloatField(required=False)
    review_scores_value = forms.FloatField(required=False)
    review_scores_communication = forms.FloatField(required=False)
    review_score_checkin = forms.FloatField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    picture_url = forms.CharField(max_length=200, required=False)
    require_guest_profile_picture = forms.IntegerField(required=False)
    is_business_travel_ready = forms.IntegerField(required=False)
    interaction = forms.CharField(widget=forms.Textarea, required=False)
    house_rules = forms.CharField(widget=forms.Textarea, required=False)
    #access_field = forms.CharField(widget=forms.Textarea, db_column='access_', blank=True,
    #                                null=True)  # Field renamed because it ended with '_'.
    beds = forms.FloatField(required=False)
    bedrooms = forms.FloatField(required=False)
    bathrooms = forms.FloatField(required=False)
    minimum_nights = forms.IntegerField(required=False)
    maximum_nights = forms.IntegerField(required=False)
    weekly_price = forms.FloatField(required=False)
    extra_people = forms.FloatField(required=False)
    monthly_price = forms.FloatField(required=False)
    guest_included = forms.IntegerField(required=False)
    security_deposit = forms.FloatField(required=False)
    cleaning_fee = forms.FloatField(required=False)
    neighborhood_overview = forms.CharField(widget=forms.Textarea, required=False)
    transit = forms.CharField(widget=forms.Textarea, required=False)
    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)

    
    class Meta:
        model = Listing
        exclude = ('id',)
    
"""

class AddListingForm(forms.ModelForm):

    host_id = forms.ModelChoiceField(queryset=Host.objects.filter(host_id__range=[3073, 32299]))

    class Meta:
        model = Listing
        fields = "__all__"

class SearchForm(forms.Form):
    FIT_CHOICE = (
        ("", "Best Match"),
        (1, "Lowest"),
        (2, "Highest")
    )

    search = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Search Listings'}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), required=False)
    city = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), required=False)
    property_type = forms.ModelChoiceField(queryset=Property.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), required=False)
    policy = forms.ModelChoiceField(queryset=Cancellation.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), required=False)
    bed_type = forms.ModelChoiceField(queryset=Beds.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), required=False)
    room_type = forms.ModelChoiceField(queryset=Rooms.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), required=False)
    price_min = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    price_max = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    size_min = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    size_max = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    bathrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    bed_min = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    bed_max = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    neighborhood = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    order = forms.ChoiceField(choices=FIT_CHOICE, widget=forms.Select(attrs={'class':'form-control'}), required=False)

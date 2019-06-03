# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Amenities(models.Model):
    amenity_id = models.BigIntegerField(primary_key=True)
    amenities = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amenities'


class Beds(models.Model):
    bed_type_id = models.BigIntegerField(primary_key=True)
    bed_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beds'

    def __str__(self):
        return self.bed_type


class Calendar(models.Model):
    calendar_id = models.BigIntegerField(primary_key=True)
    listing = models.ForeignKey('Listing', models.DO_NOTHING, blank=True, null=True)
    #listing_id = models.BigIntegerField(blank=True, null=True)
    available = models.BigIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    date_field = models.DateField(db_column='date_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'calendar'
        ordering = ["calendar_id"]


class Cancellation(models.Model):
    policy_id = models.BigIntegerField(primary_key=True)
    cancellation_policy = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancellation'

    def __str__(self):
        return self.cancellation_policy


class City(models.Model):
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country = models.CharField(max_length=100, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    country_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.country


class Host(models.Model):
    host_response_time = models.ForeignKey('HostResponseTime', models.DO_NOTHING, blank=True, null=True)
    host_id = models.BigIntegerField(primary_key=True)
    host_neighborhood = models.ForeignKey('Neighborhoods', models.DO_NOTHING, blank=True, null=True)
    host_url = models.CharField(max_length=200, blank=True, null=True)
    host_name = models.CharField(max_length=150, blank=True, null=True)
    host_about = models.TextField(blank=True, null=True)
    host_thumbnail_url = models.CharField(max_length=200, blank=True, null=True)
    host_since = models.DateField(blank=True, null=True)
    host_verifications_id = models.BigIntegerField(blank=True, null=True)
    host_picture_url = models.CharField(max_length=200, blank=True, null=True)
    host_response_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'host'

    def __str__(self):
        return self.host_name


class HostResponseTime(models.Model):
    host_response_time_id = models.BigIntegerField(primary_key=True)
    host_response_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'host_response_time'

    def __str__(self):
        return self.host_response_time


class HostVerifications(models.Model):
    host_verification_id = models.BigIntegerField(primary_key=True)
    host_verification = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'host_verifications'

    def __str__(self):
        return self.host_verification


class HostVerificationsMap(models.Model):
    host_verification = models.ForeignKey(HostVerifications, models.DO_NOTHING, primary_key=True, blank=True, null=True)
    host_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'host_verifications_map'


class Listing(models.Model):
    id = models.BigAutoField(primary_key=True)
    property_type = models.ForeignKey('Property', models.DO_NOTHING, blank=True, null=True)
    policy = models.ForeignKey(Cancellation, models.DO_NOTHING, blank=True, null=True)
    bed_type = models.ForeignKey(Beds, models.DO_NOTHING, blank=True, null=True)
    room_type = models.ForeignKey('Rooms', models.DO_NOTHING, blank=True, null=True)
    host_id = models.ForeignKey('Host', models.DO_NOTHING, blank=True, null=True, db_column='host_id')
    neighborhood = models.ForeignKey('Neighborhoods', models.DO_NOTHING, blank=True, null=True)
    listing_url = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    square_feet = models.FloatField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    space = models.TextField(blank=True, null=True)
    accomodates = models.BigIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    review_scores_accuracy = models.FloatField(blank=True, null=True)
    review_scores_rating = models.FloatField(blank=True, null=True)
    review_scores_cleanliness = models.FloatField(blank=True, null=True)
    review_scores_location = models.FloatField(blank=True, null=True)
    review_scores_value = models.FloatField(blank=True, null=True)
    review_scores_communication = models.FloatField(blank=True, null=True)
    review_score_checkin = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    picture_url = models.CharField(max_length=200, blank=True, null=True)
    require_guest_profile_picture = models.BigIntegerField(blank=True, null=True)
    is_business_travel_ready = models.BigIntegerField(blank=True, null=True)
    interaction = models.TextField(blank=True, null=True)
    house_rules = models.TextField(blank=True, null=True)
    access_field = models.TextField(db_column='access_', blank=True, null=True)  # Field renamed because it ended with '_'.
    beds = models.FloatField(blank=True, null=True)
    bedrooms = models.FloatField(blank=True, null=True)
    bathrooms = models.FloatField(blank=True, null=True)
    minimum_nights = models.BigIntegerField(blank=True, null=True)
    maximum_nights = models.BigIntegerField(blank=True, null=True)
    weekly_price = models.FloatField(blank=True, null=True)
    extra_people = models.FloatField(blank=True, null=True)
    monthly_price = models.FloatField(blank=True, null=True)
    guest_included = models.BigIntegerField(blank=True, null=True)
    security_deposit = models.FloatField(blank=True, null=True)
    cleaning_fee = models.FloatField(blank=True, null=True)
    neighborhood_overview = models.TextField(blank=True, null=True)
    transit = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False

        db_table = 'listing'




class ListingAmenitiesMap(models.Model):
    listing = models.ForeignKey(Listing, models.DO_NOTHING, primary_key=True)
    amenity = models.ForeignKey(Amenities, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'listing_amenities_map'
        unique_together = (('listing', 'amenity'),)


class Neighborhoods(models.Model):
    neighborhood_id = models.BigIntegerField(primary_key=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    neighborhood = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neighborhoods'

    def __str__(self):
        return self.neighborhood


class Property(models.Model):
    property_type_id = models.BigIntegerField(primary_key=True)
    property_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'

    def __str__(self):
        return self.property_type


class Reviewers(models.Model):
    reviewer_id = models.BigIntegerField(primary_key=True)
    reviewer_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'reviewers'
        unique_together = (('reviewer_id', 'reviewer_name'),)

    def __str__(self):
        return str(self.reviewer_name)


class Reviews(models.Model):
     #listing_id = models.BigIntegerField(blank=True, null=True)
     id = models.BigIntegerField(primary_key=True)
     date_field = models.DateField(db_column='date_', blank=True, null=True)  # Field renamed because it ended with '_'.
     listing = models.ForeignKey(Listing, models.DO_NOTHING, blank=True, null=True)
     reviewer_name = models.BigIntegerField(blank=True, null=True)
     #reviewer_name = models.ForeignKey(Reviewers, models.DO_NOTHING, db_column='reviewer_name', blank=True, null=True)
     comments = models.TextField(blank=True, null=True)
#
     class Meta:
         managed = False
         db_table = 'reviews'


class Rooms(models.Model):
    room_type_id = models.BigIntegerField(primary_key=True)
    room_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'

    def __str__(self):
        return self.room_type

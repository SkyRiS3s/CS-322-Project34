from django.test import TestCase

# Create your tests here.

def predifined_view(request):
    L = Listing
    LA = ListingAmenitiesMap
    H = Host
    # price = L.objects.filter(bedrooms=8).aggregate(Avg('price'))

    #2
    # score_cleanliness = LA.objects.filter(amenity__amenities="TV").aggregate(Avg("listing__review_scores_cleanliness"))

    #3
    # host_avail = Calendar.objects.filter(date_field__range=["2019-03-01", "2019-09-30"])
    # listing_avail = L.objects.filter(id__in=host_avail)

    #5
    #host = H.objects.filter(host_name="Viajes Eco")
    #listi = L.objects.filter(host_id__in=host)
    #avail_list = Calendar.objects.filter(listing_id__in=listi, available=1)

    #10
    #top10 = L.objects.filter(neighborhood__city__city_id__range=[1,22]).order_by("-review_scores_rating")[0:10]
    #print(top10)

    #9
    #occurance = H.objects.values('host_name','host_id').annotate(Count('host_name')).order_by('-host_name__count')[0:10]

    #6
    #one_listing = L.objects.values('host_id').annotate(Count('host_id')).filter(host_id__count=1)

    #7
    #ave_wifi_diff = abs(LA.objects.filter(amenity__amenities="Wifi").aggregate(Avg("listing__price"))['listing__price__avg'] - LA.objects.filter(~Q(amenity__amenities="Wifi")).aggregate(Avg("listing__price"))['listing__price__avg'])

    #8
    #cost_less_more = abs(L.objects.filter(beds=8, neighborhood__city__country__country_id=2).aggregate(Avg("price"))['price__avg'] - L.objects.filter(beds=8, neighborhood__city__city_id__range=[32,43]).aggregate(Avg("price"))['price__avg'])

    return render(request, 'blog/predefined_list.html', locals())
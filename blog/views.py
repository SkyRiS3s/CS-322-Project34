from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from django.contrib import messages
from .forms import AddListingForm, SearchForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Avg, Count

# Create your views here.
def home(request):
    context = {
        'countries' : Country.objects.all()
    }
    return render(request, 'blog/home.html', context)

def listing(request):
    listings_obj = Listing.objects.values("picture_url", "id", "name", "neighborhood__neighborhood", "neighborhood__city__city",
                                          "price", "property_type__property_type", "review_scores_value").order_by("id")
    paginator = Paginator(listings_obj, 6)
    page = request.GET.get('page')
    listings = paginator.get_page(page)
    return render(request, 'blog/listing.html', locals())

def listing_single(request, id):
    listing = get_object_or_404(Listing, id=id)
    reviews = Reviews.objects.filter(listing=listing)[0:5]
    if request.method == "POST":
        Listing.objects.get(id=id).delete()
        messages.error(request, 'Listing removed.')
        return redirect(reverse("listing"))
    return render(request, 'blog/listing_single.html', locals())

def host(request, host_id):
    host = get_object_or_404(Host, host_id=host_id)
    return render(request, "blog/host.html", locals())

def add_listing(request):
    form = AddListingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            f = form.save(commit=False)
            f.id = Listing.objects.latest('id').id + 1
            form.save()
            messages.add_message(request, messages.INFO, 'Listings saved.')
            return redirect(reverse("listing"))
        else: print(form.errors)
    return render(request, 'blog/add-listing.html', locals())

def predefined_view(request):

    L = Listing
    LA = ListingAmenitiesMap
    H = Host
    C = Calendar
    #1
    price = L.objects.filter(bedrooms=8).values("price").aggregate(Avg('price'))['price__avg']

    #2
    score_cleanliness = LA.objects.filter(amenity__amenities="TV").values("listing__review_scores_cleanliness").aggregate(Avg("listing__review_scores_cleanliness"))['listing__review_scores_cleanliness__avg']

    #3 out

    #5
    host = H.objects.filter(host_name="Viajes Eco")
    avail_list = C.objects.filter(listing__host_id__in=host, available=1)

    #6
    #one_listing = L.objects.values('host_id','host_id__host_name').annotate(Count('host_id')).filter(host_id__count=1)

    #7
    ave_wifi_diff = abs(LA.objects.filter(amenity__amenities="Wifi").aggregate(Avg("listing__price"))['listing__price__avg'] - LA.objects.filter(~Q(amenity__amenities="Wifi")).aggregate(Avg("listing__price"))['listing__price__avg'])

    #8
    cost_less_more = abs(L.objects.filter(beds=8, neighborhood__city__country__country_id=2).aggregate(Avg("price"))['price__avg'] - L.objects.filter(beds=8, neighborhood__city__city_id__range=[32,43]).aggregate(Avg("price"))['price__avg'])
    
    #9
    occurance = H.objects.filter(host_neighborhood__city__country_id=1).values('host_name','host_id').annotate(Count('host_name')).order_by('-host_name__count')[0:10]

    return render(request, 'blog/predefined_list.html', locals())

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def listing_search(request):
    search_value = request.GET['search'].strip()
    listings = Listing.objects.filter(Q(name__icontains=search_value) | Q(room_type__room_type__icontains=search_value) |
                                      Q(property_type__property_type__icontains=search_value))[:5]
    return render(request, 'blog/listing.html', locals())


def advanced_search(request):
    filter_dict = {}
    form = SearchForm(request.GET)
    page = 1
    listings = None
    if request.GET.get('search'):
        filter_dict['name__icontains'] = request.GET.get("search")
        if request.GET.get("price_max") or request.GET.get("price_min"):
            max_price = request.GET.get("price_max");  min_price = request.GET.get("price_min")
            if max_price and min_price:
                filter_dict['price__range'] = [min_price, max_price]
            elif max_price:
                filter_dict['price'] = float(max_price)
            elif min_price:
                filter_dict['price'] = float(min_price)
        if request.GET.get("bedrooms"):
            filter_dict['bedrooms'] = float(request.GET.get("bedrooms"))
        if request.GET.get("bathrooms"):
            filter_dict['bathrooms'] = float(request.GET.get("bathrooms"))
        if request.GET.get("bed_min") or request.GET.get("bed_max"):
            if request.GET.get("bed_max") and request.GET.get("bed_min"):
                filter_dict['beds__range'] = [request.GET.get("bed_min"), request.GET.get("bed_max")]
            elif request.GET.get("bed_min"):
                filter_dict['beds'] = request.GET.get("bed_min")
            elif request.GET.get("bed_max"):
                filter_dict['beds'] = request.GET.get("bed_max")
        if request.GET.get("size_min") or request.GET.get("size_min"):
            if request.GET.get("size_min") and request.GET.get("size_max"):
                filter_dict['square_feet__range'] = [request.GET.get("size_min"), request.GET.get("size_max")]
            elif request.GET.get("size_min"):
                filter_dict['square_feet'] = request.GET.get("size_feet")
            elif request.GET.get("size_max"):
                filter_dict['square_feet'] = request.GET.get("size_max")
        if request.GET.get("bed_type"):
            filter_dict['bed_type__bed_type_id'] = request.GET.get("bed_type")
        if request.GET.get("room_type"):
            filter_dict['room_type__room_type_id'] = request.GET.get("room_type")
        if request.GET.get("property_type"):
            filter_dict['property_type__property_type_id'] = request.GET.get("property_type")
        if request.GET.get("policy"):
            filter_dict["policy__policy_id"] = request.GET.get("policy")
        if request.GET.get("country"):
            filter_dict['neighborhood__city__country__country_id'] = request.GET.get("country")
        if request.GET.get("city"):
            filter_dict['neighborhood__city__city'] = request.GET.get("city")
        if request.GET.get("neighborhood"):
            filter_dict['neighborhood__neighborhood'] = request.GET.get("neighborhood")
        if request.GET.get("order"):
            order = request.GET.get("order")
            if order == "1":
                listings = Paginator(Listing.objects.filter(**filter_dict).order_by("price"), 6)
            elif order == "2":
                listings = Paginator(Listing.objects.filter(**filter_dict).order_by("-price"), 6)
            else:
                listings = Paginator(Listing.objects.filter(**filter_dict), 6)
        else:
            listings = Paginator(Listing.objects.filter(**filter_dict), 6)
        if not listings:
            print("aaa")
            listings = Paginator(Listing.objects.filter(**filter_dict), 6)
        if request.GET.get("page"):
            page = request.GET.get("page")
        filter_dict['order'] = request.GET.get("order")
        print("aa", filter_dict)
        form.initial = filter_dict
        listings = listings.get_page(page)
        return render(request, "blog/advance_search.html", {'listings':listings, 'searched':True, 'form':form})
    
    return render(request, 'blog/advance_search.html', locals())


def query_three(request):
    list_avail = Calendar.objects.filter(date_field__range=["2019-03-01", "2019-09-30"]).order_by("listing").values("listing__host_id__host_name", "listing__host_id__host_id").exclude(listing__host_id__host_id=None).distinct()
    paginator = Paginator(list_avail, 20)
    total_num = [str(x) for x in range(1, paginator.num_pages+1)]
    current_num = request.GET.get('page')
    list_avail = paginator.get_page(current_num)
    return render(request, 'blog/query_three.html', {'listing':list_avail, 'total_num':total_num, 'current_num':current_num})

def query_five(request):
    one_listing = Listing.objects.values('host_id','host_id__host_name').annotate(Count('host_id')).filter(host_id__count=1)
    paginator = Paginator(one_listing, 20)
    total_num = [str(x) for x in range(1, paginator.num_pages+1)]
    current_num = request.GET.get('page')
    list_avail = paginator.get_page(current_num)
    return render(request, 'blog/query_three.html', {'listing':list_avail, 'total_num':total_num, 'current_num':current_num})
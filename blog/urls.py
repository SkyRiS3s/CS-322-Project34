from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('listing/', views.listing, name='listing'),
    path('add-listing/', views.add_listing, name='add-listing'),
    path('listing/<int:id>', views.listing_single, name="listing-single"),
    path('listing/search/', views.listing_search, name="listing-search"),
    path('host/<int:host_id>', views.host, name='host'),
    path('predefined-view', views.predefined_view, name='predefined'),
    path('predefined-view/query-three', views.query_three, name='query-three'),
    path('predefined-view/query-five', views.query_three, name='query-five'),
    path('advanced-search', views.advanced_search, name='search'),
    path('about/', views.about, name='blog-about'),
]

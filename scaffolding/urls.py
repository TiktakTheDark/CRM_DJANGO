
from django.urls import path
from . import views
from scaffolding.views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('customer/', CustomerListView.as_view()),
    path('customer/<int:pk>/', CustomerDetailView.as_view()),
    path('customer/create/', CustomerCreateView.as_view()),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view()),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view()),
    
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('article/', ArticleCreateView.as_view()),
    
    path('offer/', OfferListView.as_view()),
    path('offer/create/', OfferCreateView.as_view()),
    path('offer/<int:pk>/', OfferDetailView.as_view()),
    path('offer/<int:pk>/update/', OfferUpdateView.as_view()),
    
    path('test/', Test.as_view()),
    path('test2/', TestCreateOrderView.as_view()),
]
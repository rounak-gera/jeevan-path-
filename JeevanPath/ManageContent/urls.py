from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomeSectionViewSet, AccommodationViewSet, OffersViewSet,
    GellaryImagesViewSet, ContactUsViewSet, SliderImagesViewSet,
    UpcomingFacilitiesViewSet, BlogListView, BlogDetailView, AboutUsViewSet, DiningViewSet, ContactFormViewSet
)

router = DefaultRouter()
router.register(r'home-sections', HomeSectionViewSet)
router.register(r'accommodations', AccommodationViewSet)
router.register(r'offers', OffersViewSet)
router.register(r'gallery', GellaryImagesViewSet)
router.register(r'contact', ContactUsViewSet)
router.register(r'sliders', SliderImagesViewSet)
router.register(r'upcoming-facilities', UpcomingFacilitiesViewSet)
router.register(r'about-us', AboutUsViewSet)
router.register(r'dining', DiningViewSet)
router.register(r'contact-forms', ContactFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]
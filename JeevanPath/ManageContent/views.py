from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import (
    HomeSection, Accommodation, Offers, GellaryImages,
    ContactUs, SliderImages, UpcomingFacilities, Blog,
    AboutUs, Dining, ContactForm
)
from .serializers import (
    HomeSectionSerializer, AccommodationSerializer, OffersSerializer,
    GellaryImagesSerializer, ContactUsSerializer, SliderImagesSerializer,
    UpcomingFacilitiesSerializer, BlogListSerializer, BlogDetailSerializer,
    AboutUsSerializer, DiningSerializer, ContactFormSerializer
)


class HomeSectionViewSet(viewsets.ModelViewSet):
    queryset = HomeSection.objects.all()
    serializer_class = HomeSectionSerializer


class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


class OffersViewSet(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer


class GellaryImagesViewSet(viewsets.ModelViewSet):
    queryset = GellaryImages.objects.all()
    serializer_class = GellaryImagesSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class SliderImagesViewSet(viewsets.ModelViewSet):
    queryset = SliderImages.objects.all()
    serializer_class = SliderImagesSerializer


class UpcomingFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = UpcomingFacilities.objects.all()
    serializer_class = UpcomingFacilitiesSerializer


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogListSerializer


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class DiningViewSet(viewsets.ModelViewSet):
    queryset = Dining.objects.all()
    serializer_class = DiningSerializer

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer


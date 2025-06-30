from rest_framework import serializers
from .models import (
    HomeSection, Accommodation, Offers, GellaryImages,
    ContactUs, SliderImages, UpcomingFacilities, Blog,
    AboutUs, Dining, ContactForm
)


class HomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSection
        fields = '__all__'


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = '__all__'


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'


class GellaryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GellaryImages
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class SliderImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImages
        fields = '__all__'


class UpcomingFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingFacilities
        fields = '__all__'


class BlogListSerializer(serializers.ModelSerializer):
    """Serializer for listing blogs with limited content"""
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'category', 'created_at', 'updated_at']


class BlogDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailed blog view with full content"""
    class Meta:
        model = Blog
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class DiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dining
        fields = '__all__'

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'
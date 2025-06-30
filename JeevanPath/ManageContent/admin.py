from django.contrib import admin
from . import models as app_models
from django.utils.html import format_html

class BaseModelAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        # Call delete() on each object individually to trigger media cleanup
        for obj in queryset:
            obj.delete()

class HomeSectionAdmin(BaseModelAdmin):
    list_display = ('title', 'button_name', 'image_preview')
    search_fields = ('title',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'


class AccommodationAdmin(BaseModelAdmin):
    list_display = ('title', 'button_name', 'image_preview')
    search_fields = ('title',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'button_name', 'redirect_to'),
        }),
        ('Description', {
            'fields': ('description',),
            'classes': ('wide',),
        }),
        ('Images', {
            'fields': ('slide_image_1', 'slide_image_2', 'slide_image_3', 'slide_image_4'),
            'description': 'Upload images for the accommodation carousel',
        }),
    )
    
    def image_preview(self, obj):
        if obj.slide_image_1:
            return format_html('<img src="{}" width="100" />', obj.slide_image_1.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'


class OffersAdmin(BaseModelAdmin):
    list_display = ('title', 'location', 'image_preview')
    search_fields = ('title', 'location')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'


class GalleryImagesAdmin(BaseModelAdmin):
    list_display = ('title_display', 'image_preview')
    search_fields = ('title',)
    
    def title_display(self, obj):
        if obj.title:
            return obj.title
        return f"Gallery Image {obj.id}" if obj.id else "New Gallery Image"
    title_display.short_description = 'Title'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'


class ContactUsAdmin(BaseModelAdmin):
    list_display = ('title', 'email', 'phone_number', 'address')
    search_fields = ('title', 'email', 'phone_number', 'address')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'address'),
        }),
        ('Description', {
            'fields': ('description',),
            'classes': ('wide',),
        }),
        ('Contact Information', {
            'fields': ('email', 'alternative_email', 'phone_number', 'alternative_phone_number'),
        }),
        ('Social Media Links', {
            'fields': ('facebook_link', 'instagram_link', 'twitter_link', 
                      'linkedin_link', 'youtube_link', 'whatsapp_link'),
            'classes': ('collapse',),
        }),
    )


class SliderImagesAdmin(BaseModelAdmin):
    list_display = ('title_display', 'image_preview')
    search_fields = ('title',)
    
    def title_display(self, obj):
        if obj.title:
            return obj.title
        return f"Slider Image {obj.id}" if obj.id else "New Slider Image"
    title_display.short_description = 'Title'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'


class UpcomingFacilitiesAdmin(BaseModelAdmin):
    list_display = ('title', 'location', 'expected_opening_date', 'image_preview')
    search_fields = ('title', 'location')
    list_filter = ('expected_opening_date',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'location', 'expected_opening_date'),
        }),
        ('Description', {
            'fields': ('description',),
        }),
        ('Image', {
            'fields': ('image',),
        }),
        ('Contact Information', {
            'fields': ('email', 'phone_number', 'alternative_phone_number'),
        }),
        ('Button Details', {
            'fields': ('button_name', 'redirect_to'),
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'


class BlogAdmin(BaseModelAdmin):
    list_display = ('title', 'category', 'image_preview'
    '' , 'created_at', 'updated_at')
    search_fields = ('title', 'category')
    list_filter = ('category', 'created_at')
    fieldsets = (
        ('Blog Information', {
            'fields': ('title', 'category', 'image'),
        }),
        ('Content', {
            'fields': ('blog_body',),
            'classes': ('wide',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ('created_at', 'updated_at')

class DiningAdmin(BaseModelAdmin):
    list_display = ('title', 'image_preview')
    search_fields = ('title',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title',),
        }),
        ('Description', {
            'fields': ('description',),
            'classes': ('wide',),
        }),
        ('Image', {
            'fields': ('image',),
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

class ContactFormAdmin(BaseModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone_number'),
        }),
        ('Message', {
            'fields': ('notes',),
            'classes': ('wide',),
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

class AboutUsAdmin(BaseModelAdmin):
    list_display = ('title', 'image_preview')
    search_fields = ('title',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title',),
        }),
        ('Description', {
            'fields': ('description',),
            'classes': ('wide',),
        }),
        ('Image', {
            'fields': ('image',),
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'


# Register all models with their custom admin classes
admin.site.register(app_models.HomeSection, HomeSectionAdmin)
admin.site.register(app_models.Accommodation, AccommodationAdmin)
admin.site.register(app_models.Offers, OffersAdmin)
admin.site.register(app_models.GellaryImages, GalleryImagesAdmin)
admin.site.register(app_models.ContactUs, ContactUsAdmin)
admin.site.register(app_models.SliderImages, SliderImagesAdmin)
admin.site.register(app_models.UpcomingFacilities, UpcomingFacilitiesAdmin)
admin.site.register(app_models.Blog, BlogAdmin)
admin.site.register(app_models.Dining, DiningAdmin)
admin.site.register(app_models.ContactForm, ContactFormAdmin)
admin.site.register(app_models.AboutUs, AboutUsAdmin)
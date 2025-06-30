from imghdr import what
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class HomeSection(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to='home_section/')
    button_name = models.CharField(max_length=100)
    redirect_to = models.URLField()

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = HomeSection.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    old_instance.image.delete(save=False)
            except HomeSection.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Home Section"
        verbose_name_plural = "Home Sections"

class Accommodation(models.Model):
    title = models.CharField(max_length=400)
    description = CKEditor5Field('Description', config_name='extends')
    slide_image_1 = models.ImageField('Image 1',upload_to='accommodation/')
    slide_image_2 = models.ImageField('Image 2',upload_to='accommodation/',null=True, blank=True)
    slide_image_3 = models.ImageField('Image 3',upload_to='accommodation/',null=True, blank=True)
    slide_image_4 = models.ImageField('Image 4',upload_to='accommodation/',null=True, blank=True)
    button_name = models.CharField(max_length=100)
    redirect_to = models.URLField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Accommodation.objects.get(pk=self.pk)
                if old_instance.slide_image_1 and old_instance.slide_image_1 != self.slide_image_1:
                    old_instance.slide_image_1.delete(save=False)
                if old_instance.slide_image_2 and old_instance.slide_image_2 != self.slide_image_2:
                    old_instance.slide_image_2.delete(save=False)
                if old_instance.slide_image_3 and old_instance.slide_image_3 != self.slide_image_3:
                    old_instance.slide_image_3.delete(save=False)
                if old_instance.slide_image_4 and old_instance.slide_image_4 != self.slide_image_4:
                    old_instance.slide_image_4.delete(save=False)
            except Accommodation.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.slide_image_1:
            self.slide_image_1.delete(save=False)
        if self.slide_image_2:
            self.slide_image_2.delete(save=False)
        if self.slide_image_3:
            self.slide_image_3.delete(save=False)
        if self.slide_image_4:
            self.slide_image_4.delete(save=False)
        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = "Accommodation"
        verbose_name_plural = "Accommodations"

class Offers(models.Model):
    title = models.CharField(max_length=400)
    description = CKEditor5Field('Description', config_name='extends')
    image = models.ImageField(upload_to='offers/')
    location = models.CharField(max_length=400)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Offers.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    old_instance.image.delete(save=False)
            except Offers.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

class GellaryImages(models.Model):
    image = models.ImageField(upload_to='gellary/')
    title = models.CharField(max_length=400)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return f"Gallery Image {self.id}" if self.id else "New Gallery Image"
    
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = GellaryImages.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    old_instance.image.delete(save=False)
            except GellaryImages.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

class ContactUs(models.Model):
    title = models.CharField(max_length=400)
    description = CKEditor5Field('Description', config_name='extends')
    email = models.EmailField()        
    alternative_email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    alternative_phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=400)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)

    def __str__(self):
        if self.title:
            return self.title

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

class AboutUs(models.Model):
    title = models.CharField(max_length=400)
    description = CKEditor5Field('Description', config_name='extends')
    image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        if self.title:
            return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = AboutUs.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image!= self.image:
                    old_instance.image.delete(save=False)
            except AboutUs.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

class SliderImages(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    title = models.CharField(max_length=400)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return f"Slider Image {self.id}" if self.id else "New Slider Image"
    
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = SliderImages.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    old_instance.image.delete(save=False)
            except SliderImages.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = "Slider Image"
        verbose_name_plural = "Slider Images"

class UpcomingFacilities(models.Model):
    image = models.ImageField(upload_to='upcoming_facilities/')
    title = models.CharField(max_length=400)
    description = models.TextField()
    location = models.CharField(max_length=400)
    expected_opening_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    alternative_phone_number = models.CharField(max_length=20, blank=True, null=True)
    button_name = models.CharField(max_length=100)
    redirect_to = models.URLField()

    def __str__(self):
        if self.title:
            return self.title
    
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = UpcomingFacilities.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    old_instance.image.delete(save=False)
            except UpcomingFacilities.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = "Upcoming Facility"
        verbose_name_plural = "Upcoming Facilities"

class Dining(models.Model):
    title = models.CharField(max_length=400)
    description = CKEditor5Field('Description', config_name='extends')
    image = models.ImageField(upload_to='dining/')

    def __str__(self):
        if self.title:
            return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Dining.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image!= self.image:
                    old_instance.image.delete(save=False)
            except Dining.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Dining"
        verbose_name_plural = "Dining"

class Blog(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='blog_banner/',null=True)
    category = models.CharField(max_length=100)
    blog_body = CKEditor5Field('Blog Body', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.title:
            return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Blog.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    old_instance.image.delete(save=False)
            except Blog.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Form - {self.name}"
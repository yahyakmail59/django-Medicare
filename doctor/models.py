from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name    

class Doctor(models.Model):    
    # DOCTOR_TYPE = (
    #     ('Cardiologists', 'Cardiologists'),
    #     ('Neurologists', 'Neurologists'),
    #     ('Pediatricians', 'Pediatricians'),
    #     ('Physiatrists', 'Physiatrists'),
    #     ('Dermatologists', 'Dermatologists'),
    # )
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    image = models.ImageField(upload_to='doctor/')
    name =  models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    educations_and_degrees = models.TextField(max_length=1000, null=True, blank=True)
    # department = models.CharField(max_length=200, choices=DOCTOR_TYPE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank= True)
    # department_image = models.ForeignKey("Department", on_delete=models.CASCADE, null=True, blank=True)
    # department_name = models.ForeignKey("Department", on_delete=models.CASCADE)
    degree = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    opening_time_Mon_to_Fri = models.TimeField(null=True, blank=True)
    closing_time_Mon_to_Fri = models.TimeField(null=True, blank=True)
    opening_time_Saturday = models.TimeField(null=True, blank=True)
    closing_time_Saturday = models.TimeField(null=True, blank=True)
    opening_time_Sunday = models.TimeField(null=True, blank=True)
    closing_time_Sunday = models.TimeField(null=True, blank=True)
    facebook_account = models.CharField(max_length=200, null=True, blank=True)
    twitter_account = models.CharField(max_length=200, null=True, blank=True)
    google_plus_account = models.CharField(max_length=200, null=True, blank=True)
    youtube_account = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Doctor,self).save(*args, **kwargs)
    
    # degrees = models.CharField(, max_length=50)
    class Meta:
        """Meta definition for doctor."""

        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'

    def __str__(self):
        return self.name

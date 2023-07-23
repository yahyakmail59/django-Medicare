from django.db import models
from doctor.models import Category
from django.utils.text import slugify
# Create your models here.

class Department(models.Model):
    image = models.ImageField(upload_to='department/')
    name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank= True)
    description = models.TextField(max_length=200, null=True, blank=True)
    additional_notes = models.TextField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Department,self).save(*args, **kwargs)
    
    
    def __str__(self):
        return str(self.name)
    
class DepartmentGallery(models.Model):
    department = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='department/gallary', max_length=255)

    def __str__(self):
        return str(self.department.name)
    
    class Meta:
        verbose_name = 'departmentgallery'
        verbose_name_plural = 'department gallery'
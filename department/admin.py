from django.contrib import admin
from .models import Department, DepartmentGallery
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class DepartmentGalleryInline(admin.TabularInline):
    model = DepartmentGallery
    extra = 1
    
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'slug',)
    inlines = [DepartmentGalleryInline]
    
    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(DepartmentGallery)



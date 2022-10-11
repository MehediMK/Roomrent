from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=150,verbose_name="Location")
    
    def __str__(self):
        return self.name
    

class Property(models.Model):
    title = models.CharField(max_length=50,null=False,verbose_name='Property title')
    description = models.TextField(max_length=500,null=False,verbose_name='Description')
    price = models.IntegerField(default=0,verbose_name='Price')
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,related_name='locations')
    date = models.DateTimeField(auto_now=True,verbose_name='Date')
    def __str__(self):
        return self.title
    
    
property_image_type = (
    ('BD','Bad Room'), 
    ('LR','Living Room'),
    ('BT','Bath Room'),
    ('WS','Wash Room'),
    ('DI','Dining Room'),
)

class Propertyimage(models.Model):
    image = models.ImageField(upload_to='property-image',blank=False,verbose_name='Property Image')
    type = models.CharField(max_length=50,choices=property_image_type,verbose_name='Property Type',blank=False)
    property = models.ForeignKey(Property,on_delete=models.CASCADE,blank=False,related_name='properties')
    
    def __str__(self):
        return str(self.property)
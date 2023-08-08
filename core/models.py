from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Projects_Data(models.Model):
    project_name = models.CharField(max_length=100)
    project_details = models.TextField()
    project_images = models.ImageField(upload_to='projects_images/')
    project_links = models.CharField(max_length=500) 
    project_submission_date = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return self.project_name
    
    
class BannerImages(models.Model):
    Name = models.CharField(max_length=100)
    Banner_images_Data = models.ImageField(upload_to='Banner_images/')
    
    def __str__(self):
        return self.Name

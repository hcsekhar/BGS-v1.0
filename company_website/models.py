from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
     name = models.CharField(max_length=100, null=True, blank=True)
     image = models.FileField(null=True, blank=True)
     description = models.TextField(null=True, blank=True)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.name 
class Team(models.Model):
     name = models.CharField(max_length=100, null=True, blank=True)
     image = models.FileField(null=True, blank=True)
     designation = models.CharField(max_length=100, null=True, blank=True)
     description = models.TextField(null=True, blank=True)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.name 
     
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    def __str__(self):
     return self.name
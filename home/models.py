from django.db import models

# Create your models here.
class confessions(models.Model):
    title = models.CharField(max_length=50)
    confession = models.TextField()
    
    def __str__(self):
        return self.title
    
class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.name

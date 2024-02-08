from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Item(models.Model):
        
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField()
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://theme-assets.getbento.com/sensei/bf9e806.sensei/assets/images/catering-item-placeholder-704x520.png')

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
        
    
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Snack', 'Snack'),
        ('Drink', 'Drink'),
    ]

    title = models.CharField(max_length=200)
    ingredients = models.TextField(help_text="Enter each ingredient on a new line")
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    # Optional: Foreign Key to Category model if not using choices
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

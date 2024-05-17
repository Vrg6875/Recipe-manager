from django.db import models

class vic_recipe(models.Model):
    recipe_name=models.CharField(max_length=79)
    recipe_des=models.TextField()
    recipe_image=models.ImageField(upload_to="recipe")

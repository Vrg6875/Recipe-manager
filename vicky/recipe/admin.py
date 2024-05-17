from django.contrib import admin
from recipe.models import vic_recipe # Correct import statement

class VicAdmin(admin.ModelAdmin):  # Class name should follow PEP 8 conventions
    list_display = ('recipe_name', 'recipe_des','recipe_image')

admin.site.register(vic_recipe, VicAdmin)  # Register the correct model and admin class

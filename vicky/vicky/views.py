#vicky
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('this is a debug meesage')
from recipe.models import vic_recipe
from django.contrib.auth.models import User,auth

from django.contrib import messages

def recipe(request):
       data = {}
       print('boy')
       try:
         if request.method == 'POST': 

            print('vrg')
           
            name = request.POST['recipe_name']
            des = request.POST['recipe_des']
            image = request.FILES['recipe_image']
            print('vicky')
            print(image)
            # Do something with the received data if needed
            if not all([name, des,image]):
                messages.info(request, 'All fields are required')
                return redirect('/recipe')

            vic_recipe.objects.create(recipe_name=name,recipe_des=des,recipe_image=image)
            
            data = {
                'name': name,
                'des': des,
                'image': image,
                
            }
            #en=vic_recipe(recipe_name=name,recipe_des=des,recipe_image=image)
            #en.save()
            #ya
            return HttpResponseRedirect('/recipe')
       except:

            # Return an error response
            return HttpResponse("An error occurred while processing your request.")
   
    # Always return a response, even if not in the POST method
       return render(request, "recipe.html", data)

def details(request):
    recipedata = vic_recipe.objects.all()
    data = {
        'recipedata': recipedata
    }
    d = {}  # Define d here and initialize it with an empty dictionary
    if request.method == 'POST':
        st = request.POST.get('recipename')  # Use get() method to safely retrieve POST data
        if st != None:
            recipe = vic_recipe.objects.filter(recipe_name__icontains=st)
            data['recipedata'] = recipe
          # Assigning to d inside the if block
    return render(request, "details.html", {**data, **d})  # Merge data and d into a single dictionary







def delete_recipe(request,id):
     recipedata=vic_recipe.objects.get(id=id)
     recipedata.delete()
     return HttpResponseRedirect("/details/")
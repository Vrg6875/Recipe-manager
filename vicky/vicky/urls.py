
from django.contrib import admin
from django.urls import path
from vicky import views


# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',views.recipe,name='recipe'),
    path('recipe/',views.recipe,name='recipe'),
    path('details/',views.details,name='details'),
    path('delete_recipe/<int:id>/',views.delete_recipe,name='delete_recipe')
    
   
     

    


]



#for media image ke liye Your urlpatterns here...

# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

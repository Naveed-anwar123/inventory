from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_all_items , name="items"),
    path('additem', views.additem , name="additem"),
    path('allitems', views.allitems , name="allitems"),
    path('deleteitem', views.deleteitem , name="deleteitem"),
    path('edititem', views.edititem , name="edititem"),
    path('get_single_item', views.get_single_item , name="get_single_item"),
    
    
]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_all_items , name="bitems"),
    path('additem', views.additem , name="additemb"),
    path('allitems', views.allitems , name="allitems"),
    path('deleteitem', views.deleteitem , name="deleteitemb"),
    path('edititem', views.edititem , name="edititemb"),
    path('get_single_item', views.get_single_item , name="get_single_item"),
    
]
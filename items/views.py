from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from . models import Item
from datetime import datetime
from django.core import serializers
import json as simplejson
# Create your views here.
@login_required(login_url='/accounts/login/')
def get_all_items(request):
    item_list = Item.objects.all()
    data = [{'name': o.item_name,
    'type': o.item_type,
    'subtype': o.item_subtype,
    'quantity':float(o.item_quantity),
    'price':o.item_price,
    'code': o.item_code,
    'description':o.item_description,
    'added_at': "{}".format(o.added_at.strftime("%B %d, %Y %H:%M:%S")),
    'id':o.id
    } for o in item_list] 
    return render(request , 'items/items.html' ,{'items':data})

@login_required(login_url='/accounts/login/')
def additem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        itype = request.POST.get('type')
        subtype = request.POST.get('subtype')
        code = request.POST.get('code')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        description = request.POST.get('description')

        item = Item()
        item.item_name = name
        item.item_type = itype
        item.item_subtype = subtype
        item.item_code = code
        item.item_quantity = quantity
        item.item_price = price
        item.item_description = description
        item.owner = request.user
        item.added_at = datetime.now()
        try:
                item.save()
        except Exception as identifier:
                response = {}
                response['obj'] = 'Something went wrong. Try again!'
                return JsonResponse(response)
        
        
        response = {}
        response['obj'] = 'Item added successfully!'
        return JsonResponse(response)


@login_required(login_url='/accounts/login/')
def allitems(request):
        item_list = Item.objects.all()
        #data = serializers.serialize("json", item_list, fields=('item_name'))
        
        data = [{'name': o.item_name,
                                   'type': o.item_type,
                                   'subtype': o.item_subtype,
                                   'quantity':o.item_quantity,
                                   'price':o.item_price,
                                   'code': o.item_code,
                                   'description':o.item_description,
                                   'added_at':str(o.added_at)
                                   } for o in item_list] 
        response = {}
        response["data"] = data
        return JsonResponse(response)


@login_required(login_url='/accounts/login/')
def deleteitem(request):
        Item.objects.filter(id=request.POST.get('id')).delete()
        print(request.POST.get('id'))
        response = {}
        response["obj"] = "Item deleted successfully!"
        return JsonResponse(response)

def edititem(request):
        if request.method == 'POST':
                id_ = request.POST.get('id')
                name = request.POST.get('name')
                itype = request.POST.get('type')
                subtype = request.POST.get('subtype')
                code = request.POST.get('code')
                quantity = request.POST.get('quantity')
                price = request.POST.get('price')
                description = request.POST.get('description')

               
        
                try:
                        item = Item.objects.filter(id=id_).update(item_name=name,item_type=itype,item_subtype=subtype,item_code=code,item_quantity=quantity,item_description=description,added_at=datetime.now(),item_price=price)
                except Exception as identifier:
                        response = {}
                        response['obj'] = 'Something went wrong. Try again!'
                        return JsonResponse(response)
                
                
                response = {}
                response['obj'] = 'Item Updated successfully!'
                return JsonResponse(response)


def get_single_item(request):
        item_list = Item.objects.filter(id=request.GET.get('id')).all()
        data = [{'name': o.item_name,
        'type': o.item_type,
        'subtype': o.item_subtype,
        'quantity':o.item_quantity,
        'price':o.item_price,
        'code': o.item_code,
        'description':o.item_description
        } for o in item_list] 
        response = {}
        response["data"] = data
        return JsonResponse(response)
        
from ast import Pass
from django.shortcuts import render
from .models import *
from django.db.models import Q,Max,Min
from django.core.paginator import Paginator


def index(request):
    context = {}    

    # here find max and min price from database
    max_price = Property.objects.aggregate(Max('price'))['price__max']
    context['maxprice']= max_price

    min_price = Property.objects.aggregate(Min('price'))['price__min']
    context['minprice']= min_price
    
    price = request.GET.get('price') if 'price' in request.GET else request.session['price'] if 'price' in request.session else min_price
    request.session['price'] = price 
    context['price']= price

    location = request.GET.get('location') if 'location' in request.GET else request.session['location'] if 'location' in request.session else ''
    request.session['location'] = location   
    context['location']= location
    
    # get all property data
    allproperty = ""
    allproperty = Propertyimage.objects.select_related('property').all()

    # filter by price and location
    if price or location :
        # filter by price and location if not empty
        if price != '' and location != '':
            allproperty = Propertyimage.objects.select_related('property').filter(
                Q(property_id__location__name__icontains=location) & 
                Q(property_id__price__lte=price))
            context['postcount'] = allproperty.count()
        # filter by only price if not empty
        if price != '':
            allproperty = Propertyimage.objects.select_related('property').filter(property_id__price__lte=price)
        # filter by only location if not empty
        if location != '':
            allproperty = Propertyimage.objects.select_related('property').filter(property_id__location__name__icontains=location)

    if 'orderby' in request.session:
        orderby = request.session['orderby']
        if orderby == 'lh':
            allproperty = allproperty.order_by('property_id__price')
        else:
            allproperty = allproperty.order_by('-property_id__price')
        print("Get Session",orderby)

    # get page number
    if 'price' in request.GET or 'location' in request.GET or 'page' in request.GET:
        page_number = request.GET.get('page') if 'page' in request.GET else request.session['page'] if 'page' in request.session else None

        print(page_number)
    else:
        request.session['page']=None
        request.session['price']=max_price
        del request.session['location']
        page_number=request.GET.get('page')
        request.session['page'] = page_number
    request.session['page'] = page_number
    
    # applying paginator
    paginator = Paginator(allproperty,10)            
    page_obj = paginator.get_page(page_number)
    context['properties']=page_obj

    return render(request,'index.html',context)



# for filter by order
def post_filter(request):
    # here use session for filter by heigh to low 
    orderby_value = request.GET['orderby']
    request.session['orderby'] = orderby_value
    context = {}    

    # here find max and min price from database
    max_price = Property.objects.aggregate(Max('price'))['price__max']
    context['maxprice']= max_price

    min_price = Property.objects.aggregate(Min('price'))['price__min']
    context['minprice']= min_price
    
    price = request.GET.get('price') if 'price' in request.GET else request.session['price'] if 'price' in request.session else min_price
    request.session['price'] = price 
    context['price']= price

    location = request.GET.get('location') if 'location' in request.GET else request.session['location'] if 'location' in request.session else ''
    request.session['location'] = location   
    context['location']= location
    
    # get all property data
    allproperty = ""
    allproperty = Propertyimage.objects.select_related('property').all()

    # filter by price and location
    if price or location :
        # filter by price and location if not empty
        if price != '' and location != '':
            allproperty = Propertyimage.objects.select_related('property').filter(Q(property_id__location__name__icontains=location) & Q(property_id__price__lte=price))
            context['postcount'] = allproperty.count()
        # filter by only price if not empty
        if price != '':
            allproperty = Propertyimage.objects.select_related('property').filter(property_id__price__lte=price)
        # filter by only location if not empty
        if location != '':
            allproperty = Propertyimage.objects.select_related('property').filter(property_id__location__name__icontains=location)

    

    # get page number
    if 'price' in request.GET or 'location' in request.GET or 'page' in request.GET:
        page_number = request.GET.get('page') if 'page' in request.GET else request.session['page'] if 'page' in request.session else None

        print(page_number)
    else:
        request.session['page']=None
        request.session['price']=max_price
        del request.session['location']
        page_number=request.GET.get('page')
        request.session['page'] = page_number
    request.session['page'] = page_number

    if 'orderby' in request.session:
        orderby = request.session['orderby']
        if orderby == 'lh':
            allproperty = allproperty.order_by('property_id__price')
        else:
            allproperty = allproperty.order_by('-property_id__price')
        print("Get Session",orderby)
    
    # applying paginator
    paginator = Paginator(allproperty,10)            
    page_obj = paginator.get_page(page_number)
    context['properties']=page_obj

    return render(request,'filter.html',context)
# Django Clinic Project
## Steps to build the project
### 1. Create virtual environment
```bash
mkvirtualenv erb7
```
### 2. create project
```hash
django-admin startproject erb7 .
```
### 3. Install requirements


### 4. run the server

```py
from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import district_choices,room_choices,rooms_choices
from django.db.models import Q
# Create your views here.

def listings(request):
    listings = Listing.objects.order_by('list_date').filter(is_published=True)
    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context = {'listings':paged_listings}
    return render(request,'listings/listings.html',context)

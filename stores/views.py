from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm
import requests
from django.http import HttpResponse, JsonResponse

def omdb(request):
    query = request.GET.get("q")
    if query:
        url = f"http://www.omdbapi.com/?s={query}&apikey=381068d0"
    else:
        url = "http://www.omdbapi.com/?t=twilight&apikey=381068d0"
    response = requests.get(url).json()
    context={"response": response}

    return render(request, 'omdb.html', context)

def omdb_detail(request, mov_id):
    response = requests.get(f"http://www.omdbapi.com/?i={mov_id}&apikey=381068d0").json()
    context = {
        "response": response
    }
    return render(request, 'omdb_detail.html', context)

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)


def create_store(request):
    form = StoreModelForm()
    if request.method == "POST":
        form = StoreModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)


def store_detail(request, store_slug):
    store = Store.objects.get(slug=store_slug)
    context = {
        "store": store,
    }
    return render(request, 'detail.html', context)
